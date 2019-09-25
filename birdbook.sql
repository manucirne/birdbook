-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `birdbook` ;

-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `birdbook` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
USE `birdbook` ;-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `birdbook` ;

-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `birdbook` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
USE `birdbook` ;

-- -----------------------------------------------------
-- Table `birdbook`.`CIDADE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`CIDADE` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`CIDADE` (
  `cidade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cidade`));


-- -----------------------------------------------------
-- Table `birdbook`.`USUARIO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`USUARIO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`USUARIO` (
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `fk_USUARIO_ENDERECO1`
    FOREIGN KEY (`cidade`)
    REFERENCES `birdbook`.`CIDADE` (`cidade`));


-- -----------------------------------------------------
-- Table `birdbook`.`PASSARO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`PASSARO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`PASSARO` (
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  `especie` VARCHAR(45) NULL,
  `nome_popular` VARCHAR(45) NULL,
  PRIMARY KEY (`tag_PASSARO`));


-- -----------------------------------------------------
-- Table `birdbook`.`USUARIO_PREFERE_PASSARO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`USUARIO_PREFERE_PASSARO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`USUARIO_PREFERE_PASSARO` (
  `username` VARCHAR(45) NOT NULL,
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`username`, `tag_PASSARO`),
  CONSTRAINT `fk_USUARIO_PREFERE_PASSARO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `birdbook`.`USUARIO` (`username`),
  CONSTRAINT `fk_USUARIO_PREFERE_PASSARO_PASSARO1`
    FOREIGN KEY (`tag_PASSARO`)
    REFERENCES `birdbook`.`PASSARO` (`tag_PASSARO`));


-- -----------------------------------------------------
-- Table `birdbook`.`POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`POST` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`POST` (
  `idPOST` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `texto` VARCHAR(255) NULL,
  `URL_foto` VARCHAR(100) NULL,
  `deleta` TINYINT NOT NULL,
  PRIMARY KEY (`idPOST`));


-- -----------------------------------------------------
-- Table `birdbook`.`TAG_PASSARO_POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`TAG_PASSARO_POST` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`TAG_PASSARO_POST` (
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  `idPOST` INT NOT NULL,
  PRIMARY KEY (`tag_PASSARO`, `idPOST`),
  CONSTRAINT `fk_TAG_PASSARO_PASSARO1`
    FOREIGN KEY (`tag_PASSARO`)
    REFERENCES `birdbook`.`PASSARO` (`tag_PASSARO`),
  CONSTRAINT `fk_TAG_PASSARO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `birdbook`.`POST` (`idPOST`));


-- -----------------------------------------------------
-- Table `birdbook`.`ACESSO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`ACESSO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`ACESSO` (
  `idACESSO` INT NOT NULL AUTO_INCREMENT,
  `IP` VARCHAR(45) NULL,
  `Browser` VARCHAR(45) NULL,
  `Aparelho` VARCHAR(45) NULL,
  PRIMARY KEY (`idACESSO`));


-- -----------------------------------------------------
-- Table `birdbook`.`VISUALIZACAO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`VISUALIZACAO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`VISUALIZACAO` (
  `idACESSO` INT NOT NULL,
  `idPOST` INT NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `stamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idACESSO`, `idPOST`, `stamp`),
  CONSTRAINT `fk_VISUALIZACAO_ACESSO1`
    FOREIGN KEY (`idACESSO`)
    REFERENCES `birdbook`.`ACESSO` (`idACESSO`),
  CONSTRAINT `fk_VISUALIZACAO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `birdbook`.`POST` (`idPOST`),
  CONSTRAINT `fk_VISUALIZACAO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `birdbook`.`USUARIO` (`username`));


-- -----------------------------------------------------
-- Table `birdbook`.`TAG_USUARIO_POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`TAG_USUARIO_POST` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`TAG_USUARIO_POST` (
  `username` VARCHAR(45) NOT NULL,
  `idPOST` INT NOT NULL,
  PRIMARY KEY (`username`, `idPOST`),
  CONSTRAINT `fk_TAG_USUARIO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `birdbook`.`USUARIO` (`username`),
  CONSTRAINT `fk_TAG_USUARIO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `birdbook`.`POST` (`idPOST`));

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- Table `birdbook`.`CIDADE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`CIDADE` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`CIDADE` (
  `cidade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cidade`));


-- -----------------------------------------------------
-- Table `birdbook`.`USUARIO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`USUARIO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`USUARIO` (
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `fk_USUARIO_ENDERECO1`
    FOREIGN KEY (`cidade`)
    REFERENCES `birdbook`.`CIDADE` (`cidade`));


-- -----------------------------------------------------
-- Table `birdbook`.`PASSARO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`PASSARO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`PASSARO` (
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  `especie` VARCHAR(45) NULL,
  `nome_popular` VARCHAR(45) NULL,
  PRIMARY KEY (`tag_PASSARO`));


-- -----------------------------------------------------
-- Table `birdbook`.`USUARIO_PREFERE_PASSARO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`USUARIO_PREFERE_PASSARO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`USUARIO_PREFERE_PASSARO` (
  `username` VARCHAR(45) NOT NULL,
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`username`, `tag_PASSARO`),
  CONSTRAINT `fk_USUARIO_PREFERE_PASSARO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `birdbook`.`USUARIO` (`username`),
  CONSTRAINT `fk_USUARIO_PREFERE_PASSARO_PASSARO1`
    FOREIGN KEY (`tag_PASSARO`)
    REFERENCES `birdbook`.`PASSARO` (`tag_PASSARO`));


-- -----------------------------------------------------
-- Table `birdbook`.`POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`POST` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`POST` (
  `idPOST` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `texto` VARCHAR(255) NULL,
  `URL_foto` VARCHAR(100) NULL,
  `deleta` TINYINT NOT NULL,
  PRIMARY KEY (`idPOST`));


-- -----------------------------------------------------
-- Table `birdbook`.`TAG_PASSARO_POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`TAG_PASSARO_POST` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`TAG_PASSARO_POST` (
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  `idPOST` INT NOT NULL,
  PRIMARY KEY (`tag_PASSARO`, `idPOST`),
  CONSTRAINT `fk_TAG_PASSARO_PASSARO1`
    FOREIGN KEY (`tag_PASSARO`)
    REFERENCES `birdbook`.`PASSARO` (`tag_PASSARO`),
  CONSTRAINT `fk_TAG_PASSARO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `birdbook`.`POST` (`idPOST`));


-- -----------------------------------------------------
-- Table `birdbook`.`ACESSO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`ACESSO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`ACESSO` (
  `idACESSO` INT NOT NULL AUTO_INCREMENT,
  `IP` VARCHAR(45) NULL,
  `Browser` VARCHAR(45) NULL,
  `Aparelho` VARCHAR(45) NULL,
  PRIMARY KEY (`idACESSO`));


-- -----------------------------------------------------
-- Table `birdbook`.`VISUALIZACAO`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`VISUALIZACAO` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`VISUALIZACAO` (
  `idACESSO` INT NOT NULL,
  `idPOST` INT NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `stamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idACESSO`, `idPOST`, `stamp`),
  CONSTRAINT `fk_VISUALIZACAO_ACESSO1`
    FOREIGN KEY (`idACESSO`)
    REFERENCES `birdbook`.`ACESSO` (`idACESSO`),
  CONSTRAINT `fk_VISUALIZACAO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `birdbook`.`POST` (`idPOST`),
  CONSTRAINT `fk_VISUALIZACAO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `birdbook`.`USUARIO` (`username`));


-- -----------------------------------------------------
-- Table `birdbook`.`TAG_USUARIO_POST`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `birdbook`.`TAG_USUARIO_POST` ;

CREATE TABLE IF NOT EXISTS `birdbook`.`TAG_USUARIO_POST` (
  `username` VARCHAR(45) NOT NULL,
  `idPOST` INT NOT NULL,
  PRIMARY KEY (`username`, `idPOST`),
  CONSTRAINT `fk_TAG_USUARIO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `birdbook`.`USUARIO` (`username`),
  CONSTRAINT `fk_TAG_USUARIO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `birdbook`.`POST` (`idPOST`));

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
