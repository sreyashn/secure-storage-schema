import os
from CustomHash import encrypt,decrypt,create_key
from flask import current_app as app
from werkzeug.utils import secure_filename
import  database as db
import hashlib

import base64
import  uuid
from shutil import copyfile
from datetime import datetime,timedelta

def create_tag(data):
    tag = hashlib.sha512(hashlib.sha512(data.encode("ascii")).hexdigest().encode("ascii")).hexdigest()
    return tag

def write_to_file(text,filename):
    fh = open(filename, "wb")
    fh.write(base64.b64decode(text))
    fh.close()
    # file = open(filename,"w")
    # file.write(text)
    # file.close()

def check_duplication(tag):
    # for dir,subdir,filenames in os.walk('uploads'):
    #     for filename in filenames:
    #         data = open(filename,"r").read()
    # hash = create_tag(data)
    q = "select * from file where tag='%s'" % tag
    res = db.select(q)
    print(res)
    if(len(res) > 0):
        return True,res[0]['file_id']
    else:
        return False,None

def upload(data,name,emp_id):
    # print(data)
    unique = str(uuid.uuid4())
    filename =  "uploads" + "/" + secure_filename(unique + "." + name.split(".")[-1])
    duplicate_filename =  "duplicate" + "/" + secure_filename(unique + "." + name.split(".")[-1])
    tag = create_tag(data)
    created = False
    duplicated,file_id = check_duplication(tag)
    print(duplicated,file_id)
    key = None
    if not duplicated :
        key = str(create_key())
        enc_text = encrypt(data, key)

        fh = open(duplicate_filename, "wb")
        fh.write(base64.b64decode(enc_text))
        fh.close()

        fh = open(filename, "wb")
        fh.write(base64.b64decode(enc_text))
        fh.close()

        # write_to_file(enc_text, duplicate_filename)
        # write_to_file(enc_text,filename)
        q = "insert into file(`file_path`,`date`,`status`,`key`,`tag`,`filename`)values('%s',now(),'%s','%s','%s','%s')" %(filename,'active',key,tag,name)
        file_id = db.insert(q)
        q = "insert into duplicates(`file_id`,dup_filename,emp_id)values('%s','%s','%s')" % (file_id,duplicate_filename,emp_id)
        db.insert(q)
        created = True
    else:
        q = "select * from file where file_id='%s'" % file_id
        result = db.select(q)
        key = result[0]['key']
        enc_text = encrypt(data, key)
        fh = open(duplicate_filename, "wb")
        fh.write(base64.b64decode(enc_text))
        fh.close()
        # write_to_file(enc_text, duplicate_filename)
        q = "insert into duplicates(`file_id`,dup_filename,emp_id)values('%s','%s','%s')" % (file_id, duplicate_filename,emp_id)
        db.insert(q)
    q="insert into ownership(emp_id,file_id, filename) values('%s','%s', (select filename from file where file_id = '%s'))" %(emp_id,file_id, file_id)
    # print (q)
    db.insert(q)
    return True

def restore(file_id,emp_id):
    q = "delete from ownership where file_id='%s' and emp_id='%s'" % (file_id,emp_id)
    db.delete(q)
    q = "select * from duplicates where file_id='%s'and emp_id='%s'" % (file_id,emp_id)
    result = db.select(q)
    filename = result[0]['dup_filename']

    with open(filename, "rb") as imageFile:
        data = base64.b64encode(imageFile.read()).decode('utf-8')

    delete_file(filename)
    q = "delete from duplicates where dup_filename='%s' and emp_id='%s'" % (filename,emp_id)
    db.delete(q)
    q = "select * from file where file_id='%s'" % file_id
    result = db.select(q)
    key = result[0]['key']
    # data = decrypt(data,key)
    filename = result[0]['filename']
    return upload(data,filename,emp_id)

def download(file_id):
    q = "select * from file where file_id = '%s'" % file_id
    res = db.select(q)
    key = res[0]['key']
    # file = open(res[0]['file_path'],"r")
    with open(res[0]['file_path'], "rb") as imageFile:
        data = base64.b64encode(imageFile.read()).decode('utf-8')
    # data= file.read()
    data = decrypt(data,key)
    # file1 = open("static/temp/" + os.path.basename(res[0]['file_path']),"w" )
    # file1.write(data)
    # file1.close()
    # file.close()
    # return "static/temp/" + os.path.basename(res[0]['file_path'])
    return data, os.path.basename(res[0]['file_path'])

def del_all_exp_files():
    date = (datetime.today()  - timedelta(days=7)).strftime('%Y-%m-%d')
    q = "select * from file inner join duplicates using(file_id) where date < '%s'" % date
    res = db.select(q)
    ids = []
    for row in res:
        ids.append(str(row['dup_id']))
        delete_file(row['dup_filename'])

    q = "delete from duplicates where dup_id in %s" % ("("+",".join(ids)+")")
    return db.update(q)

def get_all_exp_files():
    date = (datetime.today()  - timedelta(days=7)).strftime('%Y-%m-%d')
    q = "select * from file inner join duplicates using(file_id) where date < '%s'" % date
    return db.select(q)


def delete(file_id):
    q = "select * from  file where file_id='%s'" % file_id
    res = db.select(q)
    file_path = res[0]['file_path']
    delete_file(file_path)
    q = "delete from file where file_id='%s'" % file_id
    db.delete(q)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)