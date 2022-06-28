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
-- Dumping data for table `jalousienstatus`
--

LOCK TABLES `jalousienstatus` WRITE;
/*!40000 ALTER TABLE `jalousienstatus` DISABLE KEYS */;
INSERT INTO `jalousienstatus` VALUES (6,20,'{\'dps\': {\'1\': \'stop\', \'2\': 20, \'8\': \'forward\', \'10\': 60}}',1,'2022-06-06 16:18:24'),(7,26,'{\'dps\': {\'1\': \'close\', \'2\': 20, \'8\': \'forward\', \'10\': 60}}',1,'2022-06-06 16:28:24'),(8,37,'{\'dps\': {\'1\': \'stop\', \'2\': 0, \'8\': \'forward\', \'10\': 60}}',1,'2022-06-06 16:58:32'),(9,28,'{\'dps\': {\'1\': \'stop\', \'2\': 0, \'8\': \'forward\', \'10\': 60}}',1,'2022-06-06 16:59:02'),(10,34,'{\'dps\': {\'1\': \'stop\', \'2\': 0, \'8\': \'forward\', \'10\': 60}}',1,'2022-06-08 16:39:30'),(11,34,'{\'dps\': {\'1\': \'stop\', \'2\': 0, \'8\': \'forward\', \'10\': 60}}',1,'2022-06-08 16:40:13');
/*!40000 ALTER TABLE `jalousienstatus` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-08 17:12:33
