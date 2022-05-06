-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: foodfighters
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient` (
  `IngredientID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`IngredientID`),
  UNIQUE KEY `IngredientID_UNIQUE` (`IngredientID`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5628 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (33,'all-purpose flour'),(11,'barbeque sauce'),(15,'beef bouillon granules'),(16,'black pepper'),(21,'brown sugar'),(1,'can white tuna'),(26,'cayenne pepper'),(17,'chopped carrots'),(14,'chopped celery'),(13,'chopped onion'),(30,'cream cheese'),(12,'cubed beef stew meat '),(8,'curry powder'),(7,'dried dill weed'),(5,'dried onion flakes'),(24,'dried oregano'),(6,'dried parsley'),(19,'egg noodles'),(35,'eggs'),(23,'fresh grated ginger'),(9,'garlic powder'),(36,'heavy cream'),(2,'mayonnaise'),(22,'minced garlic'),(27,'paprika'),(4,'Parmesan cheese'),(25,'red pepper flakes'),(32,'salt'),(28,'skinless chicken thighs'),(20,'soy sauce'),(10,'St. Louis-style pork ribs'),(3,'sweet pickle relish'),(29,'unsalted butter'),(34,'vanilla extract'),(18,'water'),(31,'white sugar');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pantry`
--

DROP TABLE IF EXISTS `pantry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pantry` (
  `PantryUserID` int DEFAULT NULL,
  `PantryIngredientID` int DEFAULT NULL,
  KEY `IngredientID_idx` (`PantryIngredientID`),
  KEY `UserID_idx` (`PantryUserID`),
  CONSTRAINT `PantryIngredientID` FOREIGN KEY (`PantryIngredientID`) REFERENCES `ingredient` (`IngredientID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `PantryUserID` FOREIGN KEY (`PantryUserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pantry`
--

LOCK TABLES `pantry` WRITE;
/*!40000 ALTER TABLE `pantry` DISABLE KEYS */;
/*!40000 ALTER TABLE `pantry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quantity`
--

DROP TABLE IF EXISTS `quantity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quantity` (
  `QRecipeID` int NOT NULL,
  `QIngredientID` int NOT NULL,
  `value` float DEFAULT NULL,
  `measurement` varchar(45) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  KEY `RecipeID_idx` (`QRecipeID`),
  KEY `IngredientID_idx` (`QIngredientID`),
  CONSTRAINT `IngredientID` FOREIGN KEY (`QIngredientID`) REFERENCES `ingredient` (`IngredientID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `RecipeID` FOREIGN KEY (`QRecipeID`) REFERENCES `recipe` (`RecipeID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quantity`
--

LOCK TABLES `quantity` WRITE;
/*!40000 ALTER TABLE `quantity` DISABLE KEYS */;
INSERT INTO `quantity` VALUES (1,1,7,'ounce','drained or flaked'),(1,2,6,'tablespoon',NULL),(1,3,3,'tablespoon',NULL),(1,4,1,'tablespoon',NULL),(1,5,0.125,'teaspoon',NULL),(1,6,1,'tablespoon',NULL),(1,7,1,'teaspoon',NULL),(1,8,0.25,'teaspoon',NULL),(1,9,1,'pinch',NULL),(2,10,4,'pound','cut into 6-inch sections'),(2,11,2,'cup','or to taste'),(3,12,1,'pound',NULL),(3,13,1,'cup',NULL),(3,14,1,'cup',NULL),(3,15,0.25,'cup',NULL),(3,16,1,'pinch',NULL),(3,17,1,'cup',NULL),(3,18,5.75,'cup',NULL),(3,19,2.5,'cup',NULL),(3,6,0.25,'teaspoon',NULL),(4,20,1,'cup',NULL),(4,21,1,'cup',NULL),(4,22,4,'clove','minced'),(4,23,1,'tablespoon',NULL),(4,24,1,'tablespoon',NULL),(4,25,1,'teaspoon',NULL),(4,26,1,'teaspoon',NULL),(4,27,1,'teaspoon',NULL),(4,28,5,'pound',NULL),(4,13,1,'',NULL),(4,18,1,'cup',NULL),(4,16,1,'tablespoon',NULL),(5,29,1,'tablespoon','or as needed'),(5,30,24,'ounce','softened'),(5,31,1,'cup',NULL),(5,32,0.5,'teaspoon',NULL),(5,33,3,'tablespoon',NULL),(5,34,0.5,'teaspoon',NULL),(5,35,4,NULL,'at room temperature'),(5,36,1.25,'cup',NULL);
/*!40000 ALTER TABLE `quantity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `RecipeID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` mediumtext,
  `totalTime` int DEFAULT NULL,
  `author` int NOT NULL DEFAULT '0',
  `servingSize` int NOT NULL,
  PRIMARY KEY (`RecipeID`),
  UNIQUE KEY `RecipeID_UNIQUE` (`RecipeID`),
  KEY `author_idx` (`author`),
  CONSTRAINT `UserID` FOREIGN KEY (`author`) REFERENCES `user` (`UserID`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1366 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'Barbie\'s Tuna Salad','A unique tuna salad using curry powder and Parmesan cheese.',10,1,4),(2,'Easy St. Louis-Style Pork Ribs on Gas Grill','Easy and delicious backyard ribs made by you. Get ready to enjoy a delicious, messy dinner!',196,1,8),(3,'Beef Noodle Soup','This delicious soup was a favorite of mine while attending college. My family has been enjoying it ever since! Very easy and quick to make. It includes stew meat, mixed vegetables and egg noodles in a beef broth base. ',50,1,6),(4,'Shoyu Chicken','Shoyu Chicken is a popular Hawaiian dish. It is often served with rice. The word shoyu is Japanese for soy sauce. Let the chicken soak in the marinade for at least an hour, the longer the better.',100,1,12),(5,'\"Burnt\" Basque Cheesecake','I rarely post a trendy recipe while it\'s still trendy. But this \'burnt\' cheesecake method deserved the hype; baking it in a very hot oven delivers a beautiful, dark exterior full of bittersweet notes that make the light, creamy cheesecake interior seem even more rich and flavorful. Plus, this method is just plain easier--just remember the parchment paper. So, if you\'ve not had much luck with traditional cheesecake methods, you should stop trying and make this exclusively. ',65,1,10);
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `steps`
--

DROP TABLE IF EXISTS `steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `steps` (
  `order` int NOT NULL,
  `direction` mediumtext NOT NULL,
  `StepsRecipeID` int DEFAULT NULL,
  KEY `RecipeID_idx` (`StepsRecipeID`),
  CONSTRAINT `StepsRecipeID` FOREIGN KEY (`StepsRecipeID`) REFERENCES `recipe` (`RecipeID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `steps`
--

LOCK TABLES `steps` WRITE;
/*!40000 ALTER TABLE `steps` DISABLE KEYS */;
INSERT INTO `steps` VALUES (1,'In a medium bowl, stir together the tuna, mayonnaise, relish, Parmesan cheese, and onion flakes. Season with parsley, dill, curry powder, and garlic powder. Mix well and serve with crackers or on a sandwich.',1),(1,'Heat one side of a gas grill to 300 degrees F (150 degrees C).',2),(2,'Fill a small metal can or container with water. Cover with aluminum foil; make several slits in the foil with a knife. Place on the preheated side of the grill.',2),(3,'Place ribs bone-side up on the unheated side of the grill; close grill. Cook for 1 1/2 hours. Flip ribs and continue cooking until rib meat shrinks back from the bones, about 1 1/2 hours more.',2),(4,'Baste ribs with barbeque sauce. Transfer to the heated side of the grill; cook for 2 minutes with the lid closed. Flip and baste second side with barbeque sauce. Cook for 2 minutes with the lid closed. Flip and baste first side with more barbeque sauce. Cook for 2 minutes with the lid closed.',2),(1,'In a large saucepan over medium high heat, saute the stew meat, onion and celery for 5 minutes, or until meat is browned on all sides.',3),(2,'Stir in the bouillon, parsley, ground black pepper, carrots, water and egg noodles. Bring to a boil, reduce heat to low and simmer for 30 minutes.',3),(1,'Whisk together the soy sauce, brown sugar, water, garlic, onion, ginger, black pepper, oregano, red pepper flakes, cayenne pepper, and paprika in a large glass or ceramic bowl. Add the chicken thighs, and toss to evenly coat. Cover the bowl with plastic wrap, and marinate the chicken in the refrigerator for at least 1 hour.',4),(2,'Preheat an outdoor grill for medium heat, and lightly oil the grate.',4),(3,'Remove the chicken thighs from the marinade. Discard the remaining marinade. Grill the chicken thighs on the preheated grill until cooked through, about 15 minutes per side.',4),(1,'Preheat the oven to 400 degrees F (200 degrees C).',5),(2,'Butter a 9-inch cake pan. Cut a sheet of parchment paper large enough to line the inside of the pan by a few extra inches. Butter the paper and press it into the pan, flattening any major creases. Trim away any excess paper from the sides until you have an inch or two of overhang.',5),(3,'Combine cream cheese, sugar, salt, and flour in a bowl. Stir and smear together with a spatula until very smooth and creamy. Add vanilla extract and 1 egg; whisk to combine. Whisk in remaining eggs, one at a time. Pour in heavy cream and mix until smooth.',5),(4,'Pour batter into the prepared pan. Tap the pan against the counter to burst any excess air bubbles.',5),(5,'Bake in the preheated oven until puffed, very well browned, and nearly burned on the edges, 50 to 55 minutes. Increase oven temperature to 425 degrees F (220 degrees C) in the last 10 minutes.',5),(6,'Let cheesecake cool to room temperature, at least 25 minutes. Lift out onto a plate and peel back parchment paper, using a knife or spatula if needed. Refrigerate until thoroughly chilled, 4 hours to overnight.',5);
/*!40000 ALTER TABLE `steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `UserID_UNIQUE` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','tan272@purdue.edu','admin',NULL),(2,'Custom','chen2776@purdue.edu','custom',NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-06  1:43:23
