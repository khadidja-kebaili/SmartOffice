-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: smartoffice
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `customized_jal`
--

DROP TABLE IF EXISTS `customized_jal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customized_jal` (
  `id` int NOT NULL,
  `weekday` int DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `percentage` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `friday_keyid` FOREIGN KEY (`id`) REFERENCES `friday` (`id`),
  CONSTRAINT `monday_keyid` FOREIGN KEY (`id`) REFERENCES `monday` (`id`),
  CONSTRAINT `thursday_keyid` FOREIGN KEY (`id`) REFERENCES `thursday` (`id`),
  CONSTRAINT `tuesday_keyid` FOREIGN KEY (`id`) REFERENCES `tuesday` (`id`),
  CONSTRAINT `wednesday_keyid` FOREIGN KEY (`id`) REFERENCES `wednesday` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customized_temp`
--

DROP TABLE IF EXISTS `customized_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customized_temp` (
  `id` int NOT NULL,
  `weekday` int DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `percentage` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `friday_key_id` FOREIGN KEY (`id`) REFERENCES `friday` (`id`),
  CONSTRAINT `monday_key_id` FOREIGN KEY (`id`) REFERENCES `monday` (`id`),
  CONSTRAINT `thursday_key_id` FOREIGN KEY (`id`) REFERENCES `thursday` (`id`),
  CONSTRAINT `tuesday_key_id` FOREIGN KEY (`id`) REFERENCES `tuesday` (`id`),
  CONSTRAINT `wednesday_key_id` FOREIGN KEY (`id`) REFERENCES `wednesday` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `friday`
--

DROP TABLE IF EXISTS `friday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friday` (
  `id` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `start_time` varchar(128) DEFAULT NULL,
  `end_time` varchar(128) DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `jalousien`
--

DROP TABLE IF EXISTS `jalousien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jalousien` (
  `id` int NOT NULL DEFAULT '0',
  `ip_address` varchar(45) DEFAULT NULL,
  `local_key` varchar(45) DEFAULT NULL,
  `device_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `local_key_UNIQUE` (`local_key`),
  UNIQUE KEY `device_id_UNIQUE` (`device_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `jalousienstatus`
--

DROP TABLE IF EXISTS `jalousienstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jalousienstatus` (
  `id` int NOT NULL,
  `percentage` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `jalousieid` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `monday`
--

DROP TABLE IF EXISTS `monday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monday` (
  `id` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `start_time` varchar(128) DEFAULT NULL,
  `end_time` varchar(128) DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rules`
--

DROP TABLE IF EXISTS `rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rules` (
  `id` int NOT NULL,
  `max` int DEFAULT NULL,
  `min` int DEFAULT NULL,
  `start` varchar(128) DEFAULT NULL,
  `end` varchar(128) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='				';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `standard_jal`
--

DROP TABLE IF EXISTS `standard_jal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `standard_jal` (
  `id` int NOT NULL,
  `weekday` int DEFAULT NULL,
  `monday_id` int DEFAULT NULL,
  `tuesday_id` int DEFAULT NULL,
  `wednesday_id` int DEFAULT NULL,
  `thursday_id` int DEFAULT NULL,
  `friday_id` int DEFAULT NULL,
  KEY `monday_id_idx` (`monday_id`),
  KEY `thursday_id_idx` (`thursday_id`),
  KEY `wednesday_id_idx` (`wednesday_id`),
  KEY `friday_id` (`friday_id`),
  KEY `tuesday_id` (`tuesday_id`),
  CONSTRAINT `friday_id` FOREIGN KEY (`friday_id`) REFERENCES `friday` (`id`),
  CONSTRAINT `monday_id` FOREIGN KEY (`monday_id`) REFERENCES `monday` (`id`),
  CONSTRAINT `thursday_id` FOREIGN KEY (`thursday_id`) REFERENCES `thursday` (`id`),
  CONSTRAINT `tuesday_id` FOREIGN KEY (`tuesday_id`) REFERENCES `tuesday` (`id`),
  CONSTRAINT `wednesday_id` FOREIGN KEY (`wednesday_id`) REFERENCES `wednesday` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `standard_temp`
--

DROP TABLE IF EXISTS `standard_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `standard_temp` (
  `id` int NOT NULL,
  `weekday` int DEFAULT NULL,
  `monday_id` int DEFAULT NULL,
  `tuesday_id` int DEFAULT NULL,
  `wednesday_id` int DEFAULT NULL,
  `thursday_id` int DEFAULT NULL,
  `friday_id` int DEFAULT NULL,
  KEY `friday_id_idx` (`friday_id`),
  KEY `monday_id_idx` (`monday_id`),
  KEY `wednesday_id_idx` (`wednesday_id`),
  KEY `thursday_id_idx` (`thursday_id`),
  KEY `tuesday_id_temp_idx` (`tuesday_id`),
  CONSTRAINT `friday_id_temp` FOREIGN KEY (`friday_id`) REFERENCES `friday` (`id`),
  CONSTRAINT `monday_id_temp` FOREIGN KEY (`monday_id`) REFERENCES `monday` (`id`),
  CONSTRAINT `thursday_id_temp` FOREIGN KEY (`thursday_id`) REFERENCES `thursday` (`id`),
  CONSTRAINT `tuesday_id_temp` FOREIGN KEY (`tuesday_id`) REFERENCES `tuesday` (`id`),
  CONSTRAINT `wednesday_id_temp` FOREIGN KEY (`wednesday_id`) REFERENCES `wednesday` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `temperature`
--

DROP TABLE IF EXISTS `temperature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temperature` (
  `id` int NOT NULL,
  `temperature` float DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `device_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_idx` (`device_id`),
  CONSTRAINT `id` FOREIGN KEY (`device_id`) REFERENCES `thermostate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `thermostate`
--

DROP TABLE IF EXISTS `thermostate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thermostate` (
  `id` int NOT NULL,
  `ain` varchar(45) DEFAULT NULL,
  `sid` varchar(45) DEFAULT NULL,
  `timestamp` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `thermostatstatus`
--

DROP TABLE IF EXISTS `thermostatstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thermostatstatus` (
  `id` int NOT NULL,
  `temp` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `device_id` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `thursday`
--

DROP TABLE IF EXISTS `thursday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thursday` (
  `id` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `start_time` varchar(128) DEFAULT NULL,
  `end_time` varchar(128) DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tuesday`
--

DROP TABLE IF EXISTS `tuesday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tuesday` (
  `id` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `start_time` varchar(128) DEFAULT NULL,
  `end_time` varchar(128) DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `wednesday`
--

DROP TABLE IF EXISTS `wednesday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wednesday` (
  `id` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `start_time` varchar(128) DEFAULT NULL,
  `end_time` varchar(128) DEFAULT NULL,
  `value` int DEFAULT NULL,
  PRIMARY KEY (`id`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-25 21:11:26
