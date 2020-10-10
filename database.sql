/*
SQLyog Community v10.2 
MySQL - 5.7.13-log : Database - akhil_tiktok_database
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cric_show` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cric_show`;

/*Table structure for table `hashtag` */

DROP TABLE IF EXISTS `hashtag`;

CREATE TABLE `hashtag` (
  `hash_tag_id` varchar(100) NOT NULL,
  `hashtag_name` varchar(50) NOT NULL,
  PRIMARY KEY (`hash_tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `hashtag` */

/*Table structure for table `team_user_mapping` */

DROP TABLE IF EXISTS `team_user_mapping`;

CREATE TABLE `team_user_mapping` (
  `team_id` varchar(100) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  PRIMARY KEY (`team_id`,`user_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `team_user_mapping_ibfk_1` FOREIGN KEY (`team_id`) REFERENCES `user_team_details` (`team_id`),
  CONSTRAINT `team_user_mapping_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user_detail` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `team_user_mapping` */

/*Table structure for table `user_detail` */

DROP TABLE IF EXISTS `user_detail`;

CREATE TABLE `user_detail` (
  `user_id` varchar(100) NOT NULL,
  `user_email` varchar(30),
  `user_phone_no` varchar(15) NOT NULL,
  `user_status` bit(1) NOT NULL,
  `user_created_date` datetime NOT NULL,
  `user_name` varchar(100),
  `device_id` varchar(100) NOT NULL,
  `notify_token` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`user_phone_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_detail` */

/*Table structure for table `user_role` */

DROP TABLE IF EXISTS `user_role`;

CREATE TABLE `user_role` (
  `role_id` varchar(100) NOT NULL,
  `role` varchar(15) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_role` */

/*Table structure for table `user_role_mapping` */

DROP TABLE IF EXISTS `user_role_mapping`;

CREATE TABLE `user_role_mapping` (
  `user_id` varchar(100) NOT NULL,
  `role_id` varchar(100) NOT NULL,
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_role_mapping_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_detail` (`user_id`),
  CONSTRAINT `user_role_mapping_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `user_role` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_role_mapping` */

/*Table structure for table `user_team_details` */

DROP TABLE IF EXISTS `user_team_details`;

CREATE TABLE `user_team_details` (
  `team_id` varchar(100) NOT NULL,
  `team_name` varchar(50) DEFAULT NULL,
  `team_desc` varchar(255) DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_team_details` */

/*Table structure for table `user_video_details` */

DROP TABLE IF EXISTS `user_video_details`;

CREATE TABLE `user_video_details` (
  `video_id` varchar(100) NOT NULL,
  `video_name` varchar(50) NOT NULL,
  `video_path` varchar(255) NOT NULL,
  `uploaded_date` datetime NOT NULL,
  `user_id` varchar(20) NOT NULL,
  PRIMARY KEY (`video_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_video_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_detail` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_video_details` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
