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
-- Dumping data for table `standard_temp`
--

LOCK TABLES `standard_temp` WRITE;
/*!40000 ALTER TABLE `standard_temp` DISABLE KEYS */;
INSERT INTO `standard_temp` VALUES (1,NULL,22,NULL,NULL,NULL,NULL),(2,NULL,24,NULL,NULL,NULL,NULL),(3,NULL,26,NULL,NULL,NULL,NULL),(4,NULL,NULL,6,NULL,NULL,NULL),(5,NULL,28,NULL,NULL,NULL,NULL),(6,NULL,NULL,8,NULL,NULL,NULL),(7,NULL,NULL,NULL,7,NULL,NULL),(8,NULL,NULL,NULL,NULL,6,NULL),(9,NULL,NULL,NULL,NULL,NULL,6),(10,5,NULL,NULL,NULL,NULL,40),(11,5,NULL,NULL,NULL,NULL,41),(12,5,NULL,NULL,NULL,NULL,42),(13,5,NULL,NULL,NULL,NULL,43);
/*!40000 ALTER TABLE `standard_temp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-19 17:03:47
