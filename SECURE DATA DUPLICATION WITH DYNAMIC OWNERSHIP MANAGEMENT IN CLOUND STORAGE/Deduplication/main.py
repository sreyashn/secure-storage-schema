import database as db
import uuid
from flask import Flask,render_template,request,redirect,session,url_for,send_from_directory,Response,flash
import os
import DataDuplication as dd
import base64
import hashlib
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.secret_key="gggvklkuhjujjgh"

@app.route('/')
def public_home():
    return render_template('public/public_home.html')

@app.route('/check_user',methods=['get','post'])
def check_user():
    return session['type']

@app.route('/login',methods=['get','post'])
def login():
    if 'login' in request.form:
        Username=request.form['username']
        Password=request.form['password']
        q="select * from login where username='%s' and password='%s'" %(Username,Password)
        print( q)
        result=db.select(q)
        if(len(result)>0):
            session['type']=result[0]['login_type']
            session['login_id']=result[0]['login_id']
            if result[0]['login_type'] == "admin":
                return redirect(url_for('admin_home'))
            elif result[0]['login_type'] == "employee":
                return  redirect(url_for('user_home'))
            
        else:
            flash( "Login failed. Invalid username or password")
            return render_template("public/login.html",error_msg="Faild")

    return render_template('public/login.html')


@app.route('/admin_home',methods=['get','post'])
def admin_home():
    if "login_id" in session:
        result=db.select("select * from employee")
        return render_template("admin/admin_home.html",data=result)
    return render_template("admin/admin_home.html")

@app.route('/admin_check_history',methods=['get','post'])
def admin_check_history():
    lid=session['login_id']
    if "restore" in request.args:
        req_id=request.args['req_id']
        emp_id = request.args['emp_id']
        file_id = request.args['file_id']
        return redirect(url_for('admin_check_history'))
    q="select * from (select * from restore_request  where status='pending')temp inner join file using(file_id)"
    result=db.select(q)
    return render_template('admin/admin_check_history.html',data=result)


@app.route('/admin_restore')
def admin_restore():
    if "restore" in request.args:
        emp_id = request.args['user_id']
        file_id = request.args['file_id']
        dd.restore(file_id,emp_id)
        q = "update restore_request set status='success' where file_id='%s' and user_id='%s'" % (file_id,emp_id)
        db.update(q)
        
    return redirect(url_for('admin_check_history'))

@app.route('/admin_delete_duplicate_files')
def admin_delete_duplicate_files():
    if 'action' in request.args:
        action = request.args['action']
        if action == 'delete_all':
            dd.del_all_exp_files()
            flash('Deleted successfully')
            return redirect(url_for('admin_delete_duplicate_files'))
    res = dd.get_all_exp_files()
    return render_template('admin/expired_files.html',data = res)

@app.route('/employee',methods=['get','post'])
def employee():
    if 'Registration' in request.form:
        Firstname=request.form['Firstname']
        Lastname=request.form['Lastname']
        Age=request.form['Age']
        Phone=request.form['Phone']
        Email=request.form['Email']
        Housename=request.form['Housename']
        Place=request.form['Place']
        Pincode=request.form['Pincode']
        Username=request.form['Username']
        Password=request.form['Password']
        q="select * from login where username='%s'"%(Username)
        res=db.select(q)
        if len(res)>0:
            flash('username already exsist')
        else:
            q = "insert into login(username,password,login_type,login_status) values('%s','%s','employee','Active')" %(Username,Password)
            print( q)
            login_id=db.insert(q)
            q="insert into employee(login_id,first_name,last_name,age,phone,email,house_name,place,pincode) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (login_id,Firstname,Lastname,Age,Phone,Email,Housename,Place,Pincode)
            print( q)
            id=db.insert(q)
            if(id>0):
                print( "succes")
            else:
                print( "failed")
    return render_template('admin/employee.html')

@app.route('/employee_view',methods=['get','post'])
def employee_view():
    if "delete" in request.args:
        id = request.args['login_id']
        q = "delete from employee where login_id='%s'" % (id)
        print( q)
        result = db.delete(q)
        q = "delete from login where login_id='%s'" % (id)
        print( q)
        result = db.delete(q)

    q="select * from employee"

    result=db.select(q)
    print( q)
    return render_template("admin/employee_view.html",data=result)

@app.route('/admin_edit',methods=['get','post'])
def admin_edit():
    id = request.args['emp_id']
    if "update" in request.form:
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        Age = request.form['Age']
        Phone = request.form['Phone']
        Email = request.form['Email']
        Housename = request.form['Housename']
        Place = request.form['Place']
        Pincode = request.form['Pincode']
        q = "update employee set first_name='%s',last_name='%s',age='%s',phone='%s',email='%s',house_name='%s',place='%s',pincode='%s' where emp_id='%s'" %(Firstname,Lastname,Age,Phone,Email,Housename,Place,Pincode,id)
        print( q)
        res = db.update(q)
        return redirect(url_for('employee_view'))
    res = db.select("select * from employee where emp_id='%s'" % (id))
    return render_template('admin/admin_edit.html', data=res)





@app.route('/user_home',methods=['get','post'])
def user_home():
    result2={}
    lid = session['login_id']
    if "login_id" in session:

        if "delete" in request.args:
            emp_id = request.args['emp_id']
            file_id = request.args['file_id']
            q ="select * from ownership where emp_id='%s' and file_id='%s'" % (emp_id,file_id)
            res = db.select(q)
            if len(res) > 0:
                q = "delete from ownership where emp_id='%s' and file_id='%s'" % (emp_id,file_id)
                db.delete(q)
                q = "select * from ownership where file_id='%s'" % file_id
                res = db.select(q)
                if len(res) == 0:
                    dd.delete(file_id)
            return redirect(url_for('user_home'))

        elif "restore" in request.args:
            file_id=request.args['file_id']
            emp_id=request.args['emp_id']
            q="insert into restore_request (file_id,user_id,date,status)values('%s','%s',curdate(),'pending')" %(file_id,emp_id)
            result=db.insert(q)
            flash("Requested")
            return redirect(url_for('user_home'))

        q="select * from file inner join ownership using (file_id) where emp_id=(select emp_id from employee where login_id='%s')" %(lid)
        result=db.select(q)
        print( result)
        return render_template("user/user_home.html",data=result)

    return  render_template("user/user_home")


@app.route('/files',methods=['get','post'])
def files():
    if "upload" in request.form:
        file=request.files['file_path']
        lid=session['login_id']
        q = "select emp_id from employee where login_id='%s'" % (lid)
        result = db.select(q)
        empid = result[0]['emp_id']
        fn=secure_filename(file.filename)
        file.save('./static/temp/'+fn)
        with open('./static/temp/'+fn, "rb") as imageFile:
            data = base64.b64encode(imageFile.read()).decode('utf-8')
        # data = file.read()
        dd.upload (data, file.filename,empid)
        flash("Upload success ! you can restore the data within 7 days")
        return redirect(url_for('user_home'))

    return render_template('user/files.html')

@app.route('/share_file',methods=['get','post'])
def share_file():
    file_id = request.args['file_id']
    if "share" in request.args:
        
        emp_id = request.args['emp_id']
        q = "select * from ownership where file_id='%s' and emp_id='%s'"  % (file_id,emp_id)
        res = db.select(q)
        if(len(res) == 0):
            q = "insert into ownership(file_id,emp_id)values('%s','%s')"%(file_id,emp_id)
            db.insert(q)
            flash("Shared")
        else:
            flash("Already shared")
    login_id = session['login_id']
    employees = db.select("select * from employee where login_id<>'%s'" % login_id)
    return render_template('user/share_file.html',employees=employees,file_id=file_id)

@app.route('/restore_requests',methods=['get','post'])
def restore_requests():
    login_id = session['login_id']
    q  = "select *,restore_request.status as r_status from restore_request inner join file using(file_id) where user_id = (select user_id from employee where login_id='%s')" % login_id
    res = db.select(q)
    return render_template('user/user_request.html',data=res)





@app.route('/about',methods=['get','post'])
def about():
    return render_template('public/about.html')

@app.route('/projects',methods=['get','post'])
def projects():
        return render_template('public/projects.html')

@app.route('/public_contact',methods=['get','post'])
def public_contact():
    return render_template('public/public_contact.html')

@app.route('/logout',methods=['get','post'])
def logout():
    session['login_id']=0
    return render_template('public/public_home.html')


@app.route('/download')
def download():
    file_id = request.args['file_id']
    data,filename = dd.download(file_id)
    fh1 = open(filename, "wb")
    fh1.write(base64.b64decode(data))
    fh1.close()
    file = open(filename, "rb")
    data = file.read()
    return Response(data,
                    mimetype="text/plain",
                    headers={"Content-Disposition":
                                 "attachment;filename=%s" % filename})

@app.route('/user_changepass',methods=['get','post'])
def user_changepass():
    data = {}
    lid1=session['login_id']
    q="select username from login where login_id=%s " %(lid1)
    res=db.select(q)

    if "update" in request.form:
        passwd = request.form['password']
        new_pass = request.form['newpassword']
        lid=session['login_id']
        q = "update login set password = '%s' where login_id='%s' and password='%s'" % (new_pass,lid,passwd)
        print(q)
        n = db.update(q)

        if n > 0 :
            status = "success"
        else:
            status = "failed"
        data['status'] = status
        return render_template('user/user_home.html')

    return render_template('user/user_changepass.html', data=res)





# @app.route('/history_view',methods=['get','post'])
# def history_view():
#     if "login_id" in session:
#         lid = session['login_id']
#         q="select * from file inner join ownership using (file_id)"
#         result=db.select(q)
#         print( result)
#     return render_template("admin/history_view.html",data=result)




app.run(debug=True)
