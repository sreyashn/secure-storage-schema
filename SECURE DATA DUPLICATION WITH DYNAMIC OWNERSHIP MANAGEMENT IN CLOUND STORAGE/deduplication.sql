/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - deduplication
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`deduplication` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `deduplication`;

/*Table structure for table `duplicates` */

DROP TABLE IF EXISTS `duplicates`;

CREATE TABLE `duplicates` (
  `dup_id` int(11) NOT NULL AUTO_INCREMENT,
  `dup_filename` varchar(255) DEFAULT NULL,
  `file_id` int(11) DEFAULT NULL,
  `emp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`dup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `duplicates` */

insert  into `duplicates`(`dup_id`,`dup_filename`,`file_id`,`emp_id`) values (18,'duplicate/36829303-c0e0-48a8-8b46-0b5793011bd2.pdf',12,3),(20,'duplicate/3062731a-20e5-45ec-b5a9-6ac923d66423.docx',14,3),(22,'duplicate/89ed3951-3217-4239-8f6b-d0a97673b240.docx',16,5),(23,'duplicate/a9886ed2-888d-4532-8955-acb220ae543c.pdf',12,5),(24,'duplicate/104aa98c-b36c-43b5-b440-60f7ff461830.pptx',13,5),(25,'duplicate/86c33169-8d9f-4e06-a554-408cb6b3b782.JPG',17,5),(28,'duplicate/29570e88-e92a-4779-ba35-20d789409938.docx',18,8),(30,'duplicate/89941d58-c98a-4b26-b5c8-0ff1c76e1597.JPG',17,9),(31,'duplicate/8a88a62d-37f3-44c8-ab2a-fd03f79b58a4.pptx',19,3),(32,'duplicate/835947a4-6cb7-4be2-9c34-246325d4acfc.pdf',20,3),(33,'duplicate/000dbbb6-f68a-4990-8e43-b5f935344fe0.pdf',21,8),(34,'duplicate/ddf132b4-0d3a-42b1-aa0f-ab589737cf5c.docx',22,8),(35,'duplicate/1733b988-74e9-4814-881d-c061f402d2e0.docx',23,9);

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `emp_id` int(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `age` varchar(10) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `house_name` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `pincode` varchar(20) DEFAULT NULL,
  `login_id` int(20) NOT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`emp_id`,`first_name`,`last_name`,`age`,`phone`,`email`,`house_name`,`place`,`pincode`,`login_id`) values (3,'test1','test1','24','9895171513','test1@gmail.com','test1','test1','686101',3),(5,'test2','test2','25','789456','test2@gmail.com','test2','test2','686105',6),(8,'anu','ram','25','9656047110','anil@gmail.com','house','place','6548565',10),(9,'Vijay','John','21','9061122996','vijay@gmail.com','abcd','piravam','686662',11),(10,'jishnu','vijay','25','9876543210','jis@gmail.com','asfdgs','talikulam','680569',12);

/*Table structure for table `file` */

DROP TABLE IF EXISTS `file`;

CREATE TABLE `file` (
  `file_id` int(20) NOT NULL AUTO_INCREMENT,
  `file_path` varchar(5000) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `key` varchar(255) DEFAULT NULL,
  `tag` varchar(5000) DEFAULT NULL,
  `filename` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `file` */

insert  into `file`(`file_id`,`file_path`,`date`,`status`,`key`,`tag`,`filename`) values (12,'uploads/36829303-c0e0-48a8-8b46-0b5793011bd2.pdf','2019-10-12 13:48:13','active','QEY3Y7CHJMJ5QJAG','2231840640d86a9f9ce3af473f830671f50dd17c133495c41da492a704e5a254b08aea1c894036ff959598a65b07b656fcec8f91c029dc5f168b10c9611d695e','Chapter4.pdf'),(13,'uploads/2a73b360-3874-42a5-ba44-c96e08f874af.pptx','2019-10-12 13:48:38','active','KRUGNLVD4B5WAVKS','45cb167a0e386aa645a232f1e870da30b5c3e8b65fb76a5d56236f139ff17a73392a79f9a7c8873e0ce612a2ab4db9900201a973e99cab1eddeb3ee306a877d3','FaaSp012.pptx'),(14,'uploads/3062731a-20e5-45ec-b5a9-6ac923d66423.docx','2019-10-12 13:49:00','active','ZTG08GKOZFN8ERXQ','59d35c2463e5a3e8c92f9f769f5ee9e1bc0e697e3879467bc300732146cf620fbe885fd339b630b01474825786cec50d5ce506954fb467e762dc0c7a9feb0b66','CERTIFICATE.docx'),(15,'uploads/a7065658-01ed-4f49-8f18-240900b84231.pdf','2019-10-12 13:49:23','active','CWXL7C5AMH1DJTR5','ca545c7992c43fbafbb539ccf4898fa0a83a8ce2e90156fafd7e5f7ea0f5cc3c9992127e0f8bed676f9b70579acf1e9fa2ef3e1cd2906b01d2f3feeca068c9a3','index.pdf'),(16,'uploads/89ed3951-3217-4239-8f6b-d0a97673b240.docx','2019-10-12 13:50:46','active','2SENNGJNU30XA83H','49dbcf36517abcb9dbd51db155a0ee98a222186f473ca03cf74fabb3c08d6a8225045b4d7ab82eef61db1274c442955a3ce801a584f7103e7ffe267b267522d4','college fb.docx'),(17,'uploads/86c33169-8d9f-4e06-a554-408cb6b3b782.JPG','2019-10-12 13:52:14','active','4LJ5749TORQE0SCA','06e9897cc5a34abb10780755990a6587d1b2fbde7b0af6640dadd68110e56846f22e220657ba5d7fdf7014057fa1406a52095a94b23ed848e7b63b305ffd92e9','_MG_1029.JPG'),(18,'uploads/29570e88-e92a-4779-ba35-20d789409938.docx','2019-10-12 13:56:03','active','QPI4NSGN100Q9Q64','76fa96df806d79fd1624c8d8962a1eac0f5f588e89714d052a991645588d0fe7856e8d426e753db6ad4c2804f2731e798e63f4f6050e633832a97f0daeac16e4','fogcomputing.docx'),(19,'uploads/8a88a62d-37f3-44c8-ab2a-fd03f79b58a4.pptx','2019-10-12 14:01:03','active','8AK025GGMH2EKP5Q','047a138f0c610edc4f988b6642748bce2c6516d711435e7f7170bb45130adf44654031ff7fbe8d739c2bca40d1bc2189ac639d43adb5940ba228c31f5d399016','FaaSp012.pptx'),(20,'uploads/835947a4-6cb7-4be2-9c34-246325d4acfc.pdf','2019-10-12 14:01:07','active','JCTO2GFXEYZV21WO','3265eb26b7708948def6bf51a9a6961e93f7f54069bf8177b0640b04c051afdd6715bfa7964b4c256640b595b1edf7456868d1d8eeeb53dac2749e030ac11312','index.pdf'),(21,'uploads/000dbbb6-f68a-4990-8e43-b5f935344fe0.pdf','2019-10-12 14:01:14','active','RCOABXKLK524I5NX','0b950d70303704fabb715ab1270b265d7dd9cb2d7efeb263c7b7001255f9585826e8a7db34d657ad2b1986cfec3cf94df228857d1e42e629f493c18f41e3df38','index.pdf'),(22,'uploads/ddf132b4-0d3a-42b1-aa0f-ab589737cf5c.docx','2019-10-12 14:01:18','active','WC0UIX13ICI6NPWQ','982723bd91be6cbd1cfe2493449e2588b8f0752b121b124fb38772d91858b805cbd9fc2dcc7577b76af57054a7324ab8e1d370904182f9a593248da02b790e9c','college fb.docx'),(23,'uploads/1733b988-74e9-4814-881d-c061f402d2e0.docx','2019-10-12 14:01:21','active','85OAA3OCOLY1FCGL','eab93f19d4063377994e1b06f98c0f415fb113599f896e05b5ad5b2f8c9289363a7b7866b27b9f7b583204419024f454acb9f8bfda86952176750446dc188ea5','CERTIFICATE.docx');

/*Table structure for table `history` */

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `his_id` int(20) NOT NULL AUTO_INCREMENT,
  `file_id` int(20) NOT NULL,
  `date` date NOT NULL,
  `operation` varchar(40) NOT NULL,
  PRIMARY KEY (`his_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `history` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `login_type` varchar(20) DEFAULT NULL,
  `login_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`login_type`,`login_status`) values (1,'admin','admin','admin','Active'),(3,'test1','test1','employee','Active'),(6,'test2','test2','employee','Active'),(10,'anu','1234','employee','Active'),(11,'vijay','123','employee','Active'),(12,'jishnu','jishnu','employee','Active');

/*Table structure for table `ownership` */

DROP TABLE IF EXISTS `ownership`;

CREATE TABLE `ownership` (
  `file_id` int(20) NOT NULL,
  `emp_id` int(20) NOT NULL,
  `filename` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ownership` */

insert  into `ownership`(`file_id`,`emp_id`,`filename`) values (12,3,'Chapter4.pdf'),(14,3,'CERTIFICATE.docx'),(16,5,'college fb.docx'),(12,5,'Chapter4.pdf'),(13,5,'FaaSp012.pptx'),(17,5,'_MG_1029.JPG'),(18,8,'fogcomputing.docx'),(17,9,'_MG_1029.JPG'),(19,3,'FaaSp012.pptx'),(20,3,'index.pdf'),(21,8,'index.pdf'),(22,8,'college fb.docx'),(23,9,'CERTIFICATE.docx');

/*Table structure for table `restore_request` */

DROP TABLE IF EXISTS `restore_request`;

CREATE TABLE `restore_request` (
  `req_id` int(20) NOT NULL AUTO_INCREMENT,
  `file_id` int(20) NOT NULL,
  `user_id` int(20) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `restore_request` */

insert  into `restore_request`(`req_id`,`file_id`,`user_id`,`date`,`status`) values (7,13,3,'2019-10-12','success'),(8,15,3,'2019-10-12','success'),(9,14,9,'2019-10-12','success'),(10,16,8,'2019-10-12','success'),(11,15,8,'2019-10-12','success');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
