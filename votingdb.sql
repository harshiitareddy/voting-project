/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - votingdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`votingdb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `votingdb`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`password`) values ('admin','admin');

/*Table structure for table `ausers` */

DROP TABLE IF EXISTS `ausers`;

CREATE TABLE `ausers` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `uname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `adno` varchar(100) NOT NULL,
  `eimg` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `ausers` */

insert  into `ausers`(`id`,`uname`,`email`,`adno`,`eimg`) values (1,'vishwa','vishwa.9777@gmail.com','331435982741','srk.jpg'),(2,'mouli','vishwa.977@gmail.com','331435982746','srk.jpg'),(3,'raj','projecttwoiot@gmail.com','331435982743','srk.jpg');

/*Table structure for table `cand` */

DROP TABLE IF EXISTS `cand`;

CREATE TABLE `cand` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `cname` varchar(100) NOT NULL,
  `pname` varchar(100) NOT NULL,
  `img` varchar(100) NOT NULL,
  `loc` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `cand` */

insert  into `cand`(`id`,`cname`,`pname`,`img`,`loc`) values (8,'sanjay','bjp','bjp.jpg','gulbarga'),(9,'jack','congress','congress.jpeg','gulbarga');

/*Table structure for table `finalresult` */

DROP TABLE IF EXISTS `finalresult`;

CREATE TABLE `finalresult` (
  `cname` varchar(100) NOT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `img` varchar(100) DEFAULT NULL,
  `loc` varchar(100) DEFAULT NULL,
  `ccount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `finalresult` */

insert  into `finalresult`(`cname`,`pname`,`img`,`loc`,`ccount`) values ('jack','congress','congress.jpeg','gulbarga','1'),('sanjay','bjp','bjp.jpg','gulbarga','2');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `c` int(11) DEFAULT NULL,
  `cname` varchar(100) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `img` varchar(100) DEFAULT NULL,
  `loc` varchar(100) DEFAULT NULL,
  `uname` varchar(100) NOT NULL,
  PRIMARY KEY (`uname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`c`,`cname`,`pname`,`img`,`loc`,`uname`) values (1,'sanjay','bjp','bjp.jpg','gulbarga','mouli'),(1,'jack','congress','congress.jpeg','gulbarga','raj'),(1,'sanjay','bjp','bjp.jpg','gulbarga','vishwa');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
