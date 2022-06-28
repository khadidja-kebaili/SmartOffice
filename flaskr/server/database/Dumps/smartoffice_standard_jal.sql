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
-- Dumping data for table `standard_jal`
--

LOCK TABLES `standard_jal` WRITE;
/*!40000 ALTER TABLE `standard_jal` DISABLE KEYS */;
INSERT INTO `standard_jal` VALUES (1,NULL,4,NULL,NULL,NULL,NULL),(2,NULL,5,NULL,NULL,NULL,NULL),(3,NULL,NULL,1,NULL,NULL,NULL),(4,NULL,NULL,NULL,1,NULL,NULL),(5,NULL,NULL,NULL,NULL,1,NULL),(6,NULL,NULL,NULL,NULL,NULL,1),(7,NULL,23,NULL,NULL,NULL,NULL),(8,NULL,NULL,3,NULL,NULL,NULL),(9,NULL,NULL,NULL,3,NULL,NULL);
/*!40000 ALTER TABLE `standard_jal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-20 12:30:34
