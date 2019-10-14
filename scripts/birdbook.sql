-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema birdbok
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `birdbok` ;

-- -----------------------------------------------------
-- Schema birdbok
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `birdbok` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
USE `birdbok` ;

-- -----------------------------------------------------
-- Table `birdbok`.`CIDADE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`CIDADE` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`CIDADE` (
  `cidade` VARCHAR(45) NOT NULL COMMENT 'Nome da cidade',
  `estado` VARCHAR(45) NOT NULL COMMENT 'Estado ao qual a cidade pertence',
  `idCIDADE` INT NOT NULL AUTO_INCREMENT COMMENT 'Id da tabe',
  PRIMARY KEY (`idCIDADE`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `birdbok`.`USUARIO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`USUARIO` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`USUARIO` (
  `username` VARCHAR(45) NOT NULL COMMENT 'username que define o usuário - único PK',
  `email` VARCHAR(45) NOT NULL COMMENT 'Email do usuário',
  `nome` VARCHAR(45) NOT NULL COMMENT 'Nome do usuário',
  `idCIDADE` INT NOT NULL COMMENT 'Cidade em que o usuário mora',
  PRIMARY KEY (`username`))
ENGINE = InnoDB;

CREATE INDEX `fk_USUARIO_CIDADE1_idx` ON `birdbok`.`USUARIO` (`idCIDADE` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `birdbok`.`PASSARO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`PASSARO` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`PASSARO` (
  `tag_PASSARO` VARCHAR(20) NOT NULL COMMENT 'tag do pássaro',
  `especie` VARCHAR(45) NULL COMMENT 'espécie do pássaro',
  `nome_popular` VARCHAR(45) NULL COMMENT 'nome mais usual do pássaro',
  PRIMARY KEY (`tag_PASSARO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `birdbok`.`USUARIO_PREFERE_PASSARO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`USUARIO_PREFERE_PASSARO` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`USUARIO_PREFERE_PASSARO` (
  `username` VARCHAR(45) NOT NULL COMMENT 'username do usuário que prefere o pássaro',
  `tag_PASSARO` VARCHAR(20) NOT NULL COMMENT 'tag do pássaro que é preferido pelo usuário',
  PRIMARY KEY (`username`, `tag_PASSARO`))
ENGINE = InnoDB;

CREATE INDEX `fk_USUARIO_PREFERE_PASSARO_PASSARO1_idx` ON `birdbok`.`USUARIO_PREFERE_PASSARO` (`tag_PASSARO` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `birdbok`.`POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`POST` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`POST` (
  `idPOST` INT NOT NULL AUTO_INCREMENT COMMENT 'id so post',
  `titulo` VARCHAR(45) NOT NULL COMMENT 'títilo do post',
  `texto` VARCHAR(255) NULL COMMENT 'id do texto',
  `URL_foto` VARCHAR(100) NULL COMMENT 'url da foto que pode estar relacionada ao post',
  `deleta` TINYINT NOT NULL COMMENT 'define se o post foi ou não deletado, ou seja, se ele será ou não mostrado na rede social',
  PRIMARY KEY (`idPOST`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `birdbok`.`TAG_PASSARO_POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`TAG_PASSARO_POST` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`TAG_PASSARO_POST` (
  `tag_PASSARO` VARCHAR(20) NOT NULL COMMENT 'tag do pássaro que é mencionando no post',
  `idPOST` INT NOT NULL COMMENT 'id do post que menciona o pássaro',
  PRIMARY KEY (`tag_PASSARO`, `idPOST`))
ENGINE = InnoDB;

CREATE INDEX `fk_TAG_PASSARO_POST1_idx` ON `birdbok`.`TAG_PASSARO_POST` (`idPOST` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `birdbok`.`ACESSO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`ACESSO` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`ACESSO` (
  `idACESSO` INT NOT NULL AUTO_INCREMENT COMMENT 'id do acesso',
  `IP` VARCHAR(45) NULL COMMENT 'IP que foi usado para executar a visualização',
  `Browser` VARCHAR(45) NULL COMMENT 'browser que foi utilizado no acesso em que a visualização aconteceu',
  `Aparelho` VARCHAR(45) NULL COMMENT 'aparelho utilizado para executar o acesso atrelado à visualização',
  PRIMARY KEY (`idACESSO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `birdbok`.`VISUALIZACAO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`VISUALIZACAO` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`VISUALIZACAO` (
  `idACESSO` INT NOT NULL COMMENT 'id do acesso em que a visualização ocorreu',
  `idPOST` INT NOT NULL COMMENT 'id do post que foi visualizado',
  `username` VARCHAR(45) NOT NULL COMMENT 'usuário que executou a visualização',
  `stamp` TIMESTAMP(6) NOT NULL COMMENT 'momento em que a visualização aconteceu',
  PRIMARY KEY (`idACESSO`, `idPOST`, `stamp`))
ENGINE = InnoDB;

CREATE INDEX `fk_VISUALIZACAO_POST1_idx` ON `birdbok`.`VISUALIZACAO` (`idPOST` ASC) VISIBLE;

CREATE INDEX `fk_VISUALIZACAO_USUARIO1_idx` ON `birdbok`.`VISUALIZACAO` (`username` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `birdbok`.`TAG_USUARIO_POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbok`.`TAG_USUARIO_POST` ;

CREATE TABLE IF NOT EXISTS `birdbok`.`TAG_USUARIO_POST` (
  `username` VARCHAR(45) NOT NULL COMMENT 'usernema do usuário ao qual o post pertence',
  `idPOST` INT NOT NULL COMMENT 'is do post que pertence ao usuário',
  PRIMARY KEY (`username`, `idPOST`))
ENGINE = InnoDB;

CREATE INDEX `fk_TAG_USUARIO_USUARIO1_idx` ON `birdbok`.`TAG_USUARIO_POST` (`username` ASC) VISIBLE;

CREATE INDEX `fk_TAG_USUARIO_POST1_idx` ON `birdbok`.`TAG_USUARIO_POST` (`idPOST` ASC) VISIBLE;

USE `birdbok`;

DELIMITER $$

USE `birdbok`$$
DROP TRIGGER IF EXISTS `birdbok`.`USUARIO_AFTER_DELETE` $$
USE `birdbok`$$
CREATE DEFINER = CURRENT_USER TRIGGER `birdbok`.`USUARIO_AFTER_DELETE` AFTER DELETE ON `USUARIO` FOR EACH ROW
BEGIN
	DELETE FROM USUARIO_PREFERE_PASSARO
        WHERE username = OLD.username;
END$$


USE `birdbok`$$
DROP TRIGGER IF EXISTS `birdbok`.`USUARIO_AFTER_DELETE_POST` $$
USE `birdbok`$$
CREATE DEFINER = CURRENT_USER TRIGGER `birdbok`.`USUARIO_AFTER_DELETE_POST` AFTER DELETE ON `USUARIO` FOR EACH ROW
BEGIN
	UPDATE POST
		SET deleta = '1' 
        WHERE username = OLD.username;
END$$


USE `birdbok`$$
DROP TRIGGER IF EXISTS `birdbok`.`PASSARO_AFTER_DELETE` $$
USE `birdbok`$$
CREATE DEFINER = CURRENT_USER TRIGGER `birdbok`.`PASSARO_AFTER_DELETE` AFTER DELETE ON `PASSARO` FOR EACH ROW
BEGIN
	DELETE FROM USUARIO_PREFERE_PASSARO
        WHERE tag_PASSARO = OLD.tag_PASSARO;
END$$


USE `birdbok`$$
DROP TRIGGER IF EXISTS `birdbok`.`POST_AFTER_UPDATE` $$
USE `birdbok`$$
CREATE DEFINER = CURRENT_USER TRIGGER `birdbok`.`POST_AFTER_UPDATE` AFTER UPDATE ON `POST` FOR EACH ROW
BEGIN
	IF NEW.deleta = TRUE THEN
		DELETE FROM TAG_PASSARO_POST
			WHERE idPOST = NEW.idPOST;
		DELETE FROM TAG_USUARIO_POST 
			WHERE idPOST = NEW.idPOST;
		DELETE FROM VISUALIZACAO 
			WHERE idPOST = NEW.idPOST;
	END IF;
END$$


USE `birdbok`$$
DROP TRIGGER IF EXISTS `birdbok`.`VISUALIZACAO_AFTER_DELETE` $$
USE `birdbok`$$
CREATE DEFINER = CURRENT_USER TRIGGER `birdbok`.`VISUALIZACAO_AFTER_DELETE` AFTER DELETE ON `VISUALIZACAO` FOR EACH ROW
BEGIN
    DELETE FROM ACESSO 
        WHERE idACESSO = OLD.idACESSO;
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
