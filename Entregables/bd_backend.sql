CREATE DATABASE  IF NOT EXISTS `prueba_back_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `prueba_back_db`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: prueba_back_db
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `tb_empleados`
--

DROP TABLE IF EXISTS `tb_empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_empleados` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(55) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `curp` varchar(55) NOT NULL,
  `puesto` varchar(55) DEFAULT NULL,
  `clave_jefe` int DEFAULT NULL,
  `calle` varchar(55) NOT NULL,
  `numero_exterior` int NOT NULL,
  `numero_interior` int DEFAULT NULL,
  `colonia` varchar(55) NOT NULL,
  `municipio` varchar(55) NOT NULL,
  `estado` varchar(55) NOT NULL,
  `pais` varchar(55) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `clave_jefe` (`clave_jefe`),
  KEY `ix_tb_empleados_id` (`id`),
  CONSTRAINT `tb_empleados_ibfk_1` FOREIGN KEY (`clave_jefe`) REFERENCES `tb_empleados` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_empleados`
--

LOCK TABLES `tb_empleados` WRITE;
/*!40000 ALTER TABLE `tb_empleados` DISABLE KEYS */;
INSERT INTO `tb_empleados` VALUES (1,'Yolanda','Juarez','PEYOS021054874','Ceo',NULL,'Juan Escutia',150,777,'Centro','Xicotepec','Puebla','Mexico'),(2,'Daniel','Mendez','MED0971952HPLRRA','Manager',1,'Josefa Ortiz',296,NULL,'Morelos','Huachinango','Puebla','Mexico'),(3,'Lucia','Rodriguez','ROLU0971952HPLRRA','Manager',1,'Avenida Insurgentes',500,NULL,'Roma Norte','Ciudad de México','CDMX','México'),(4,'Miguel','Cruz','CRMI0971952HPLRRA','Ventas',3,'Calle Reforma',45,7,'Polanco','Ciudad de México','CDMX','México'),(5,'Rosana','Pereira','PERO0971952HPLRRA','Comunicacion',3,'Calle Benito Juárez',121,NULL,'Centro','Toluca','Estado de México','México'),(6,'Alexandra','Hernandez','HEAL0971952HPLRRA','Employee',4,'Calle Morelos',85,NULL,'Zapata','Cuernavaca','Morelos','México'),(7,'Jose Ramon','Tolentino','TOJOR0971952HPLRRA','Employee',5,'Avenida Universidad',205,5,'Jardines','Puebla','Puebla','México'),(8,'Rocio','Flores','FLRO0971952HPLRRA','Operaciones',2,'Calle Emiliano Zapata',35,NULL,'Centro','Oaxaca','Oaxaca','México'),(9,'Luis','Oliver','OLLU0971952HPLRRA','Diseno',2,'Calle Hidalgo',150,8,'Zona Centro','Guadalajara','Jalisco','México'),(10,'Jesus','Angeles','ANJE0971952HPLRRA','Employee',9,'Avenida Las Américas',108,NULL,'Miraflores','Monterrey','Nuevo Leon','México'),(11,'Claudia','Lopez','LOCA0971952HPLRRA','Employee',8,'Calle Constitución',60,NULL,'Constitución','Hermosillo','Sonora','México'),(12,'Hector','Fernandez','FEHE0971952HPLRRA','Employee',8,'Calle Independencia',258,NULL,'El Refugio','Querétaro','Querétaro','México'),(13,'Eva','Luna','LUEV0971952HPLRRA','Employee',5,'Avenida Colón',90,2,'Los Reyes','Juarez','Nuevo Leon','México'),(15,'Ramiro','Toledo','TOPY021014HPLLRRA0',NULL,NULL,'juanEscutia',10,NULL,'Morelos','Xicotepec','Puebla','Mexico');
/*!40000 ALTER TABLE `tb_empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_empleados`
--

DROP TABLE IF EXISTS `view_empleados`;
/*!50001 DROP VIEW IF EXISTS `view_empleados`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_empleados` AS SELECT 
 1 AS `id`,
 1 AS `NombreJefe`,
 1 AS `Direccion`,
 1 AS `NombreEmpleado`,
 1 AS `DireccionEmpleado`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_empleados`
--

/*!50001 DROP VIEW IF EXISTS `view_empleados`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_empleados` AS select uuid() AS `id`,concat(`jefe`.`nombres`,' ',`jefe`.`apellidos`) AS `NombreJefe`,concat(`jefe`.`calle`,',',`jefe`.`numero_exterior`,ifnull(concat(' Num. Interior',`jefe`.`numero_interior`),''),', ',`jefe`.`colonia`,', ',`jefe`.`municipio`,', ',`jefe`.`estado`,', ',`jefe`.`pais`) AS `Direccion`,concat(`sub`.`nombres`,' ',`sub`.`apellidos`) AS `NombreEmpleado`,concat(`sub`.`calle`,',',`sub`.`numero_exterior`,ifnull(concat(' Num. Interior ',`sub`.`numero_interior`),' '),', ',`sub`.`colonia`,', ',`sub`.`municipio`,', ',`sub`.`estado`,', ',`sub`.`pais`) AS `DireccionEmpleado` from (`tb_empleados` `sub` left join `tb_empleados` `jefe` on((`sub`.`clave_jefe` = `jefe`.`id`))) where (`sub`.`clave_jefe` is not null) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-15  0:43:43
