-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema projeto1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projeto1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projeto1` DEFAULT CHARACTER SET utf8 ;
USE `projeto1` ;

-- -----------------------------------------------------
-- Table `projeto1`.`ENDERECO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`ENDERECO` (
  `idENDERECO` INT NOT NULL AUTO_INCREMENT,
  `logradouro` VARCHAR(100) NULL,
  `cidade` VARCHAR(45) NULL,
  PRIMARY KEY (`idENDERECO`));


-- -----------------------------------------------------
-- Table `projeto1`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`USUARIO` (
  `username` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `idENDERECO` INT NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `fk_USUARIO_ENDERECO`
    FOREIGN KEY (`idENDERECO`)
    REFERENCES `projeto1`.`ENDERECO` (`idENDERECO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `projeto1`.`PASSARO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`PASSARO` (
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  `especie` VARCHAR(45) NULL,
  `nome_popular` VARCHAR(45) NULL,
  PRIMARY KEY (`tag_PASSARO`));


-- -----------------------------------------------------
-- Table `projeto1`.`USUARIO_PREFERE_PASSARO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`USUARIO_PREFERE_PASSARO` (
  `username` VARCHAR(45) NOT NULL,
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`username`, `tag_PASSARO`),
  CONSTRAINT `fk_USUARIO_PREFERE_PASSARO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `projeto1`.`USUARIO` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_USUARIO_PREFERE_PASSARO_PASSARO1`
    FOREIGN KEY (`tag_PASSARO`)
    REFERENCES `projeto1`.`PASSARO` (`tag_PASSARO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `projeto1`.`POST`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`POST` (
  `idPOST` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `texto` VARCHAR(255) NULL,
  `URL_foto` VARCHAR(100) NULL,
  `deleta` TINYINT NOT NULL,
  PRIMARY KEY (`idPOST`));


-- -----------------------------------------------------
-- Table `projeto1`.`TAG_PASSARO_POST`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`TAG_PASSARO_POST` (
  `tag_PASSARO` VARCHAR(20) NOT NULL,
  `idPOST` INT NOT NULL,
  PRIMARY KEY (`tag_PASSARO`, `idPOST`),
  CONSTRAINT `fk_TAG_PASSARO_PASSARO1`
    FOREIGN KEY (`tag_PASSARO`)
    REFERENCES `projeto1`.`PASSARO` (`tag_PASSARO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TAG_PASSARO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `projeto1`.`POST` (`idPOST`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `projeto1`.`ACESSO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`ACESSO` (
  `idACESSO` INT NOT NULL AUTO_INCREMENT,
  `ip` VARCHAR(45) NULL,
  `browser` VARCHAR(45) NULL,
  `aparelho` VARCHAR(45) NULL,
  PRIMARY KEY (`idACESSO`));


-- -----------------------------------------------------
-- Table `projeto1`.`VISUALIZACAO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`VISUALIZACAO` (
  `idACESSO` INT NOT NULL,
  `idPOST` INT NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `time_stamp_vis` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idACESSO`, `idPOST`, `time_stamp_vis`),
  CONSTRAINT `fk_VISUALIZACAO_ACESSO1`
    FOREIGN KEY (`idACESSO`)
    REFERENCES `projeto1`.`ACESSO` (`idACESSO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_VISUALIZACAO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `projeto1`.`POST` (`idPOST`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_VISUALIZACAO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `projeto1`.`USUARIO` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `projeto1`.`TAG_USUARIO_POST`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto1`.`TAG_USUARIO_POST` (
  `username` VARCHAR(45) NOT NULL,
  `idPOST` INT NOT NULL,
  PRIMARY KEY (`username`, `idPOST`),
  CONSTRAINT `fk_TAG_USUARIO_USUARIO1`
    FOREIGN KEY (`username`)
    REFERENCES `projeto1`.`USUARIO` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TAG_USUARIO_POST1`
    FOREIGN KEY (`idPOST`)
    REFERENCES `projeto1`.`POST` (`idPOST`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
