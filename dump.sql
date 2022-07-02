-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: my_blog
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Photo_Post`
--

DROP TABLE IF EXISTS `Photo_Post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Photo_Post` (
  `photo_id` int unsigned NOT NULL,
  `post_id` int unsigned NOT NULL,
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  KEY `photo_id` (`photo_id`),
  CONSTRAINT `Photo_Post_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `Post` (`id`) ON DELETE CASCADE,
  CONSTRAINT `Photo_Post_ibfk_2` FOREIGN KEY (`photo_id`) REFERENCES `User_Photo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Photo_Post`
--

LOCK TABLES `Photo_Post` WRITE;
/*!40000 ALTER TABLE `Photo_Post` DISABLE KEYS */;
INSERT INTO `Photo_Post` VALUES (1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5),(6,6,6),(6,7,7),(5,8,8),(4,9,9),(1,10,10),(2,11,11),(3,12,12),(3,13,13),(2,14,14),(1,15,15),(6,16,16),(5,17,17),(4,18,18),(3,19,19),(4,20,20),(2,21,21),(5,22,22),(1,23,23),(6,24,24),(4,25,25),(3,26,26),(2,27,27),(1,28,28),(5,29,29),(6,38,30),(5,39,31),(2,40,32),(3,41,33),(6,42,34),(1,43,35),(2,44,36),(3,45,37);
/*!40000 ALTER TABLE `Photo_Post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Post`
--

DROP TABLE IF EXISTS `Post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Post` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `creation_date` date NOT NULL,
  `text` text,
  `category_id` int unsigned DEFAULT NULL,
  `likes` int unsigned DEFAULT NULL,
  `view` int unsigned DEFAULT NULL,
  `shared` int unsigned DEFAULT NULL,
  `status_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `status_id` (`status_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `Post_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `Post_Status` (`id`),
  CONSTRAINT `Post_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `Category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Post`
--

LOCK TABLES `Post` WRITE;
/*!40000 ALTER TABLE `Post` DISABLE KEYS */;
INSERT INTO `Post` VALUES (1,'Pellentesque felis nibh','2022-06-01','Phasellus sit amet neque molestie nunc tincidunt ultrices. Donec laoreet mi sit amet gravida bibendum. Aliquam erat volutpat. Aliquam arcu est, malesuada a nisi in.',NULL,NULL,NULL,NULL,NULL),(2,'Mauris nisi magna, congue quis faucibus ac','2022-06-02','Nulla in tincidunt neque, a luctus mi. Donec sollicitudin est vehicula mauris condimentum mattis. Suspendisse in augue ut lorem viverra dignissim. Fusce ultrices, mauris vitae fringilla.',NULL,NULL,NULL,NULL,NULL),(3,'Adipiscing auctor turpis','2022-06-03','Aenean auctor leo et libero convallis, eget tempor urna rutrum. Aliquam erat volutpat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.',NULL,NULL,NULL,NULL,NULL),(4,'Duis sed lectus placerat, facilisis lacus id','2022-06-04','Pellentesque aliquam eros non augue cursus, ut porta leo ornare. Suspendisse odio lectus, commodo ac mauris in, bibendum pretium nisi.',NULL,NULL,NULL,NULL,NULL),(5,'Fermentum pellentesque dolor at','2022-06-05','Duis eros nisl, tincidunt sed elit ut, feugiat elementum justo. Vivamus ornare id eros vel imperdiet. Sed venenatis dapibus consequat. Curabitur viverra erat id vehicula consectetur.',NULL,NULL,NULL,NULL,NULL),(6,'Nunc sodales nec ante eget sollicitudin','2022-06-06','Pellentesque imperdiet sem nec pellentesque luctus. Sed nisl elit, tempus sed ultricies vel, laoreet ut magna. In a condimentum nulla. Maecenas sem tellus, blandit a felis at, luctus lobortis erat.',NULL,NULL,NULL,NULL,NULL),(7,'Winston S. Churchill','2022-06-01','Success is not final; failure is not fatal: It is the courage to continue that counts.',NULL,NULL,NULL,NULL,NULL),(8,'Herman Melville','2022-06-02','It is better to fail in originality than to succeed in imitation.',NULL,NULL,NULL,NULL,NULL),(9,'Colin R. Davis','2022-06-03','The road to success and the road to failure are almost exactly the same.',NULL,NULL,NULL,NULL,NULL),(10,'Henry David Thoreau','2022-06-04','Success usually comes to those who are too busy looking for it.',NULL,NULL,NULL,NULL,NULL),(11,'Dale Carnegie','2022-06-05','Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.',NULL,NULL,NULL,NULL,NULL),(12,'Calvin Coolidge','2022-06-06','Nothing in the world can take the place of Persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan \'Press On\' has solved and always will solve the problems of the human race.',NULL,NULL,NULL,NULL,NULL),(13,'Mister Rogers','2022-06-07','There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.',NULL,NULL,NULL,NULL,NULL),(14,'John Wooden','2022-06-08','Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.',NULL,NULL,NULL,NULL,NULL),(15,'Estée Lauder','2022-06-09','I never dreamed about success. I worked for it.',NULL,NULL,NULL,NULL,NULL),(16,'W. P. Kinsella','2022-06-10','Success is getting what you want, happiness is wanting what you get.',NULL,NULL,NULL,NULL,NULL),(17,'Winston Churchill','2022-06-11','The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.',NULL,NULL,NULL,NULL,NULL),(18,'Will Rogers','2022-06-12','Don’t let yesterday take up too much of today.',NULL,NULL,NULL,NULL,NULL),(19,'Unknown','2022-06-13','You learn more from failure than from success. Don’t let it stop you. Failure builds character.',NULL,NULL,NULL,NULL,NULL),(20,'Steve Jobs','2022-06-14','If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you.',NULL,NULL,NULL,NULL,NULL),(21,'Vernon Sanders Law','2022-06-15','Experience is a hard teacher because she gives the test first, the lesson afterwards.',NULL,NULL,NULL,NULL,NULL),(22,'Dorothy West','2022-06-16','To know how much there is to know is the beginning of learning to live.',NULL,NULL,NULL,NULL,NULL),(23,'Cindy Gallop','2022-06-17','Women challenge the status quo because we are never it.',NULL,NULL,NULL,NULL,NULL),(24,'Arlan Hamilton','2022-06-18','We don’t just sit around and wait for other people. We just make, and we do.',NULL,NULL,NULL,NULL,NULL),(25,'Oprah Winfrey','2022-06-19','Think like a queen. A queen is not afraid to fail. Failure is another stepping stone to greatness.',NULL,NULL,NULL,NULL,NULL),(26,'Unknown','2022-06-20','The strongest actions for a woman is to love herself, be herself and shine amongst those who never believed she could.',NULL,NULL,NULL,NULL,NULL),(27,'Yulia Tymoshenko','2022-06-21','Whenever you see a successful woman, look out for three men who are going out of their way to try to block her.',NULL,NULL,NULL,NULL,NULL),(28,'Lady Gaga','2022-06-22','Some women choose to follow men, and some choose to follow their dreams. If you’re wondering which way to go, remember that your career will never wake up and tell you that it doesn’t love you anymore.',NULL,NULL,NULL,NULL,NULL),(29,'Roseanne Barr','2022-06-23','The thing women have yet to learn is nobody gives you power. You just take it. ',NULL,NULL,NULL,NULL,NULL),(38,'T D Jakes','2022-06-24','No woman wants to be in submission to a man who isn’t in submission to God!',NULL,NULL,NULL,NULL,NULL),(39,'George Meredith','2022-06-25','A witty woman is a treasure; a witty beauty is a power.',NULL,NULL,NULL,NULL,NULL),(40,'Diane Von Furstenberg','2022-06-26','When a woman becomes her own best friend life is easier.',NULL,NULL,NULL,NULL,NULL),(41,'Margaret Thatcher','2022-06-27','If you want something said, ask a man if you want something done, ask a woman.',NULL,NULL,NULL,NULL,NULL),(42,'Sheryl Sandberg','2022-06-28','We need women at all levels, including the top, to change the dynamic, reshape the conversation, to make sure women’s voices are heard and heeded, not overlooked and ignored.',NULL,NULL,NULL,NULL,NULL),(43,'Madeleine Albright','2022-06-29','It took me quite a long time to develop a voice, and now that I have it, I am not going to be silent.',NULL,NULL,NULL,NULL,NULL),(44,'Eleanor Roosevelt','2022-06-30','Women must learn to play the game as men do.',NULL,NULL,NULL,NULL,NULL),(45,'Ayn Rand','2022-07-02','I swear, by my life and my love of it, that I will never live for the sake of another man, nor ask another man to live for mine.',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Post_Status`
--

DROP TABLE IF EXISTS `Post_Status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Post_Status` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Post_Status`
--

LOCK TABLES `Post_Status` WRITE;
/*!40000 ALTER TABLE `Post_Status` DISABLE KEYS */;
/*!40000 ALTER TABLE `Post_Status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Social_media`
--

DROP TABLE IF EXISTS `Social_media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Social_media` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `Telegram` varchar(255) DEFAULT NULL,
  `Instagram` varchar(255) DEFAULT NULL,
  `Twitter` varchar(255) DEFAULT NULL,
  `YouTube` varchar(255) DEFAULT NULL,
  `Facebook` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Social_media`
--

LOCK TABLES `Social_media` WRITE;
/*!40000 ALTER TABLE `Social_media` DISABLE KEYS */;
/*!40000 ALTER TABLE `Social_media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `pasword` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `birthday` date NOT NULL,
  `phone` varchar(255) NOT NULL,
  `status_id` int unsigned DEFAULT NULL,
  `social_media_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `status_id` (`status_id`),
  KEY `social_media_id` (`social_media_id`),
  CONSTRAINT `User_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `User_Status` (`id`) ON DELETE SET NULL,
  CONSTRAINT `User_ibfk_2` FOREIGN KEY (`social_media_id`) REFERENCES `Social_media` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'oscurik','0123456789','oscurabow@gmail.com','Dolzhenkov','Andrii','1995-05-06','+380501234556',NULL,NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Photo`
--

DROP TABLE IF EXISTS `User_Photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Photo` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) NOT NULL,
  `user_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `User_Photo_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Photo`
--

LOCK TABLES `User_Photo` WRITE;
/*!40000 ALTER TABLE `User_Photo` DISABLE KEYS */;
INSERT INTO `User_Photo` VALUES (1,'/static/blog_img/bimg_1.png',1),(2,'/static/blog_img/bimg_2.png',1),(3,'/static/blog_img/bimg_3.png',1),(4,'/static/blog_img/bimg_4.png',1),(5,'/static/blog_img/bimg_5.png',1),(6,'/static/blog_img/bimg_6.png',1);
/*!40000 ALTER TABLE `User_Photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Post`
--

DROP TABLE IF EXISTS `User_Post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Post` (
  `user_id` int unsigned NOT NULL,
  `post_id` int unsigned NOT NULL,
  KEY `user_id` (`user_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `User_Post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE,
  CONSTRAINT `User_Post_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `Post` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Post`
--

LOCK TABLES `User_Post` WRITE;
/*!40000 ALTER TABLE `User_Post` DISABLE KEYS */;
INSERT INTO `User_Post` VALUES (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(1,12),(1,13),(1,14),(1,15),(1,16),(1,17),(1,18),(1,19),(1,20),(1,21),(1,22),(1,23),(1,24),(1,25),(1,26),(1,27),(1,28),(1,29),(1,38),(1,39),(1,40),(1,41),(1,42),(1,43),(1,44),(1,45);
/*!40000 ALTER TABLE `User_Post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Status`
--

DROP TABLE IF EXISTS `User_Status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Status` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Status`
--

LOCK TABLES `User_Status` WRITE;
/*!40000 ALTER TABLE `User_Status` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_Status` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-02 15:04:05
