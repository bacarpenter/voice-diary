DROP  SCHEMA IF EXISTS `voice_diary`; -- https://www.sqlshack.com/overview-of-the-t-sql-if-exists-statement-in-a-sql-server-database/
CREATE SCHEMA `voice_diary` ;
CREATE TABLE `voice_diary`.`entries` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(128) NULL,
  `text` LONGTEXT NULL,
  `timestamp` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
