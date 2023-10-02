-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: db_mentoring
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_area`
--

DROP TABLE IF EXISTS `app_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_area` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_area`
--

LOCK TABLES `app_area` WRITE;
/*!40000 ALTER TABLE `app_area` DISABLE KEYS */;
INSERT INTO `app_area` VALUES (1,'Frontend'),(2,'Backend'),(3,'Desarrollo de carrera'),(4,'Diseño UX-UI'),(5,'Freelancing'),(6,'Introducción a la programación'),(7,'Git'),(8,'Inglés'),(9,'Mobile'),(10,'Orientación CV'),(11,'QA'),(12,'Product management'),(13,'Soft skills');
/*!40000 ALTER TABLE `app_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_meetings`
--

DROP TABLE IF EXISTS `app_meetings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_meetings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start` datetime(6) NOT NULL,
  `end` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `link` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `mentor_id` bigint NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `app_meetings_user_id_40c2f338_fk_auth_user_id` (`user_id`),
  KEY `app_meetings_mentor_id_2f1151fe_fk_app_mentor_id` (`mentor_id`),
  CONSTRAINT `app_meetings_mentor_id_2f1151fe_fk_app_mentor_id` FOREIGN KEY (`mentor_id`) REFERENCES `app_mentor` (`id`),
  CONSTRAINT `app_meetings_user_id_40c2f338_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_meetings`
--

LOCK TABLES `app_meetings` WRITE;
/*!40000 ALTER TABLE `app_meetings` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_meetings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_mentor`
--

DROP TABLE IF EXISTS `app_mentor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_mentor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` longtext NOT NULL,
  `website` varchar(200) NOT NULL,
  `github` varchar(200) NOT NULL,
  `linkedin` varchar(200) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `app_mentor_user_id_a983c5a8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_mentor`
--

LOCK TABLES `app_mentor` WRITE;
/*!40000 ALTER TABLE `app_mentor` DISABLE KEYS */;
INSERT INTO `app_mentor` VALUES (2,'Desarrolladora fullstack Python con experiencia en tutoría.\r\nEnseñé introducción a la programación por tres años en varios niveles.\r\nEspero poder serte de mucha ayuda!','','https://github.com/jessica-armoa','http://www.linkedin.com/in/jessica-armoa',17),(3,'Programador Fullstack MERN, en reunión podremos resolver errores puntuales o dudas sobre tu CV.','','https://github.com/jessica-armoa','http://www.linkedin.com/in/jessica-armoa',18),(4,'QA con 5 años de experiencia, y desarrollador Mobile, te ayudo si estas iniciando o si estas en busca de trabajo','','https://github.com/jessica-armoa','http://www.linkedin.com/in/jessica-armoa',19),(5,'jhbsac','','https://github.com/jessica-armoa','http://www.linkedin.com/in/jessica-armoa',21);
/*!40000 ALTER TABLE `app_mentor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_mentor_areas`
--

DROP TABLE IF EXISTS `app_mentor_areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_mentor_areas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mentor_id` bigint NOT NULL,
  `area_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_mentor_areas_mentor_id_area_id_51365a8c_uniq` (`mentor_id`,`area_id`),
  KEY `app_mentor_areas_area_id_c42bab35_fk_app_area_id` (`area_id`),
  CONSTRAINT `app_mentor_areas_area_id_c42bab35_fk_app_area_id` FOREIGN KEY (`area_id`) REFERENCES `app_area` (`id`),
  CONSTRAINT `app_mentor_areas_mentor_id_520dfcf3_fk_app_mentor_id` FOREIGN KEY (`mentor_id`) REFERENCES `app_mentor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_mentor_areas`
--

LOCK TABLES `app_mentor_areas` WRITE;
/*!40000 ALTER TABLE `app_mentor_areas` DISABLE KEYS */;
INSERT INTO `app_mentor_areas` VALUES (5,2,1),(6,2,2),(7,2,3),(8,2,6),(9,2,7),(10,3,1),(11,3,2),(12,3,5),(13,3,6),(14,3,10),(15,4,8),(16,4,9),(17,4,10),(18,4,11),(20,5,6),(19,5,10);
/*!40000 ALTER TABLE `app_mentor_areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add user',1,'add_mentor'),(2,'Can change user',1,'change_mentor'),(3,'Can delete user',1,'delete_mentor'),(4,'Can view user',1,'view_mentor'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add user',5,'add_user'),(18,'Can change user',5,'change_user'),(19,'Can delete user',5,'delete_user'),(20,'Can view user',5,'view_user'),(21,'Can add content type',6,'add_contenttype'),(22,'Can change content type',6,'change_contenttype'),(23,'Can delete content type',6,'delete_contenttype'),(24,'Can view content type',6,'view_contenttype'),(25,'Can add session',7,'add_session'),(26,'Can change session',7,'change_session'),(27,'Can delete session',7,'delete_session'),(28,'Can view session',7,'view_session'),(29,'Can add area',8,'add_area'),(30,'Can change area',8,'change_area'),(31,'Can delete area',8,'delete_area'),(32,'Can view area',8,'view_area'),(33,'Can add meetings',9,'add_meetings'),(34,'Can change meetings',9,'change_meetings'),(35,'Can delete meetings',9,'delete_meetings'),(36,'Can view meetings',9,'view_meetings'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (15,'pbkdf2_sha256$600000$ujWMGq90o5B8gF6eTgPtwd$IyOCPPqDh5xPfAj34Z3A0XOyKF56sO8JpymbVjW9xNE=',NULL,0,'alditus1','Aldito','Martinez','aldom@gmail.com',0,1,'2023-09-26 17:09:56.593444'),(17,'pbkdf2_sha256$600000$rZjCWp3BxbO8tt3JHhTFT6$2YtrMnsE5M/CC9tk+GJ10DB5oqwOYhbfCYGXt5Yjtq4=',NULL,0,'jessyarmoa','Jessica','Armoa','jessyarmoa@gmail.com',0,1,'2023-09-26 18:35:15.103613'),(18,'pbkdf2_sha256$600000$qckHSU13h5eoiKraKoqFDd$THFaFGI3sz8l+YOzKi+vm5MUDLX2jgDX43dlOUgyKws=',NULL,0,'danibaezgonz','Danilo','Baez','danibaezgonz@gmail.com',0,1,'2023-09-26 20:18:52.633065'),(19,'pbkdf2_sha256$600000$6jZ5nuYQlas7UghUYjCTFp$zS9+la38ZQIVbSeStrpIrGLSjxuyTUqDHuKp+Fjr/LU=',NULL,0,'danilobaez010','Fernando','Sanchez','danilobaez010@gmail.com',0,1,'2023-09-26 22:12:33.415863'),(20,'pbkdf2_sha256$600000$OZWw5MdrpyupJ9wieAUGnN$LlfoOp3KlJRZlH3KHv+BvkoVXOj6X8Wfky4ALxLZrRM=',NULL,0,'brendah','Brenda','Huemer','brendahuemer@gmail.com',0,1,'2023-09-26 23:07:34.886786'),(21,'pbkdf2_sha256$600000$mvHRiUcZo5LahJciJeAexT$i2l41IG0T/P7Wzq5S1WKfrWUHIbcxFWH1AxY4DrpBn0=',NULL,0,'yanina','Yanina','Armoa','yaninaarmoa0@gmail.com',0,1,'2023-09-27 00:58:37.038695');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'admin','logentry'),(8,'app','area'),(9,'app','meetings'),(1,'app','mentor'),(10,'app','user'),(4,'auth','group'),(3,'auth','permission'),(5,'auth','user'),(6,'contenttypes','contenttype'),(7,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-09-23 04:17:53.231923'),(2,'auth','0001_initial','2023-09-23 04:17:53.599492'),(3,'admin','0001_initial','2023-09-23 04:17:53.711486'),(4,'admin','0002_logentry_remove_auto_add','2023-09-23 04:17:53.724451'),(5,'admin','0003_logentry_add_action_flag_choices','2023-09-23 04:17:53.738594'),(6,'contenttypes','0002_remove_content_type_name','2023-09-23 04:17:53.812582'),(7,'auth','0002_alter_permission_name_max_length','2023-09-23 04:17:53.862743'),(8,'auth','0003_alter_user_email_max_length','2023-09-23 04:17:53.896498'),(9,'auth','0004_alter_user_username_opts','2023-09-23 04:17:53.908037'),(10,'auth','0005_alter_user_last_login_null','2023-09-23 04:17:53.960331'),(11,'auth','0006_require_contenttypes_0002','2023-09-23 04:17:53.964274'),(12,'auth','0007_alter_validators_add_error_messages','2023-09-23 04:17:53.977305'),(13,'auth','0008_alter_user_username_max_length','2023-09-23 04:17:54.031691'),(14,'auth','0009_alter_user_last_name_max_length','2023-09-23 04:17:54.086819'),(15,'auth','0010_alter_group_name_max_length','2023-09-23 04:17:54.117740'),(16,'auth','0011_update_proxy_permissions','2023-09-23 04:17:54.134225'),(17,'auth','0012_alter_user_first_name_max_length','2023-09-23 04:17:54.185733'),(18,'sessions','0001_initial','2023-09-23 04:17:54.212661'),(19,'app','0001_initial','2023-09-23 04:23:41.123968'),(20,'app','0002_remove_area_mentor_mentor_areas','2023-09-23 04:27:18.064331'),(21,'app','0003_alter_mentor_options_alter_mentor_managers_and_more','2023-09-23 04:50:19.708435'),(22,'app','0004_alter_meetings_mentor_user','2023-09-26 00:15:04.619624'),(23,'app','0005_delete_user','2023-09-26 03:34:36.089880');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('36ju3nqflboc9cqo5hxoi12i9zfwvnw6','eyJ1c2VyX2lkIjoyMX0:1qlIsw:8z8fGNet2LfjORG0VetnFbZtJ9KNJ3Z3Zz5tFIDaq7c','2023-10-11 00:58:38.161765'),('hinbe1lh8gxl6q6m21kshev3mx2wacyc','eyJ1c2VyX2lkIjoxN30:1qnQLF:JDNgLu652qUCzJmsvrKT-WAaYSWWOsFO9dunA4yapNE','2023-10-16 21:20:37.373993'),('jfb8htjxa7fn42ss8m5wslvzcvh18lfc','eyJ1c2VyX2lkIjoxN30:1qlcil:dRZrIqdgBMZ5KvxReB9ax-biVEos8boGDKKbRmEAGw4','2023-10-11 22:09:27.787783'),('mzpi5qc9kyp1qqiu5gjddyw0gtpqulxj','e30:1qlHGB:rZCawK0aFODL524rbF5c22gSi_YSS1xUZfDHshj6h_0','2023-10-10 23:14:31.372641');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-02 19:05:28
