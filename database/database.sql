/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;

CREATE TABLE catog
(
    id    INT(11) NOT NULL,
    title    VARCHAR(600),
    PRIMARY KEY(id)
) ENGINE = InnoDB;


CREATE TABLE game_auth
(
    user    INT(11) NOT NULL AUTO_INCREMENT,
    auth    INT(5) NOT NULL,
    final    VARCHAR(440) NOT NULL,
    PRIMARY KEY(user)
) ENGINE = InnoDB;


CREATE TABLE game_result
(
    username    VARCHAR(440) NOT NULL,
    result    INT(11) NOT NULL,
    last    INT(11) NOT NULL,
    PRIMARY KEY(username)
) ENGINE = InnoDB;

CREATE TABLE game_result
(
    username    VARCHAR(440) NOT NULL,
    result    INT(11) NOT NULL,
    last    INT(11) NOT NULL,
    PRIMARY KEY(username)
) ENGINE = InnoDB;



CREATE TABLE game_test
(
    id    INT(11) NOT NULL,
    catg    INT(11),
    title    VARCHAR(800),
    ans1    VARCHAR(400),
    ans2    VARCHAR(400),
    PRIMARY KEY(id)
) ENGINE = InnoDB;



CREATE TABLE games
(
    id    INT(11) NOT NULL AUTO_INCREMENT,
    title    VARCHAR(1020) NOT NULL,
    ans1    VARCHAR(400) NOT NULL,
    ans2    VARCHAR(400) NOT NULL,
    PRIMARY KEY(id)
) ENGINE = InnoDB;


CREATE TABLE party
(
    id    INT(11) NOT NULL AUTO_INCREMENT,
    party    VARCHAR(400) NOT NULL,
    user    VARCHAR(400) NOT NULL,
    catag    VARCHAR(200),
    PRIMARY KEY(id)
) ENGINE = InnoDB;


CREATE TABLE session
(
    party_user    VARCHAR(600) NOT NULL,
    pid    INT(11) NOT NULL,
    PRIMARY KEY(party_user)
) ENGINE = InnoDB;


CREATE TABLE temp
(
    store_by    VARCHAR(400) NOT NULL,
    data    VARCHAR(400),
    PRIMARY KEY(store_by)
) ENGINE = InnoDB;


CREATE TABLE users
(
    full_name    VARCHAR(400) NOT NULL,
    username    VARCHAR(400) NOT NULL,
    sex    VARCHAR(44) NOT NULL,
    user_id    INT(11),
    PRIMARY KEY(username)
) ENGINE = InnoDB;


CREATE TABLE party_result
(
    partyid    INT(11),
    userresult    VARCHAR(40),
    partyresult    VARCHAR(40),
    userlast    INT(11) UNSIGNED,
    partylast    INT(11) UNSIGNED
) ENGINE = InnoDB;