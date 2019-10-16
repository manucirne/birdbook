SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- DATABASE birdbook
-- -----------------------------------------------------
DROP DATABASE IF EXISTS birdbook ;

-- -----------------------------------------------------
-- DATABASE birdbook
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS birdbook DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema birdbook
-- -----------------------------------------------------
USE birdbook ;

-- -----------------------------------------------------
-- Table birdbook.CIDADE
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.CIDADE;

CREATE TABLE IF NOT EXISTS birdbook.CIDADE (
  cidade VARCHAR(45) NOT NULL COMMENT 'Nome da cidade',
  estado VARCHAR(45) NOT NULL COMMENT 'Estado ao qual a cidade pertence',
  idCIDADE INT NOT NULL AUTO_INCREMENT COMMENT 'Id da tabela',
  PRIMARY KEY (idCIDADE));



-- -----------------------------------------------------
-- Table birdbook.USUARIO
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.USUARIO ;

CREATE TABLE IF NOT EXISTS birdbook.USUARIO (
  username VARCHAR(45) NOT NULL COMMENT 'username que define o usuário - único PK',
  email VARCHAR(45) NOT NULL COMMENT 'Email do usuário',
  nome VARCHAR(45) NOT NULL COMMENT 'Nome do usuário',
  idCIDADE INT NOT NULL COMMENT 'Cidade em que o usuário mora',
  CONSTRAINT cidadeexiste FOREIGN KEY (idCIDADE)
    REFERENCES birdbook.CIDADE(idCIDADE), 
  PRIMARY KEY (username));



-- -----------------------------------------------------
-- Table birdbook.PASSARO
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.PASSARO ;

CREATE TABLE IF NOT EXISTS birdbook.PASSARO (
  tag_PASSARO VARCHAR(20) NOT NULL COMMENT 'tag do pássaro',
  especie VARCHAR(45) NULL COMMENT 'espécie do pássaro',
  nome_popular VARCHAR(45) NULL COMMENT 'nome mais usual do pássaro',
  PRIMARY KEY (tag_PASSARO));



-- -----------------------------------------------------
-- Table birdbook.USUARIO_PREFERE_PASSARO
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.USUARIO_PREFERE_PASSARO ;

CREATE TABLE IF NOT EXISTS birdbook.USUARIO_PREFERE_PASSARO (
  username VARCHAR(45) NOT NULL COMMENT 'username do usuário que prefere o pássaro',
  FOREIGN KEY (username)
    REFERENCES birdbook.USUARIO(username),
  tag_PASSARO VARCHAR(20) NOT NULL COMMENT 'tag do pássaro que é preferido pelo usuário',
  FOREIGN KEY (tag_PASSARO)
    REFERENCES birdbook.PASSARO(tag_PASSARO),
  PRIMARY KEY (username, tag_PASSARO));



-- -----------------------------------------------------
-- Table birdbook.POST
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.POST ;

CREATE TABLE IF NOT EXISTS birdbook.POST (
  idPOST INT NOT NULL AUTO_INCREMENT COMMENT 'id so post',
  titulo VARCHAR(45) NOT NULL COMMENT 'títilo do post',
  texto VARCHAR(255) NULL COMMENT 'id do texto',
  URL_foto VARCHAR(100) NULL COMMENT 'url da foto que pode estar relacionada ao post',
  deleta TINYINT NOT NULL DEFAULT 0 COMMENT 'define se o post foi ou não deletado, ou seja, se ele será ou não mostrado na rede social',
  username VARCHAR(45) NOT NULL,
  FOREIGN KEY (username)
    REFERENCES birdbook.USUARIO(username),
  PRIMARY KEY (idPOST));



-- -----------------------------------------------------
-- Table birdbook.TAG_PASSARO_POST
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.TAG_PASSARO_POST ;

CREATE TABLE IF NOT EXISTS birdbook.TAG_PASSARO_POST (
  tag_PASSARO VARCHAR(20) NOT NULL COMMENT 'tag do pássaro que é mencionando no post',
  FOREIGN KEY (tag_PASSARO)
    REFERENCES birdbook.PASSARO(tag_PASSARO),
  idPOST INT NOT NULL COMMENT 'id do post que menciona o pássaro',
  FOREIGN KEY (idPOST)
    REFERENCES birdbook.POST(idPOST),
  PRIMARY KEY (tag_PASSARO, idPOST));



USE birdbook ;

-- -----------------------------------------------------
-- Table birdbook.JOINHA
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.JOINHA ;

CREATE TABLE IF NOT EXISTS birdbook.JOINHA (
  username VARCHAR(45) NOT NULL COMMENT 'username do usuário que deu joinha no post',
  FOREIGN KEY (username)
    REFERENCES birdbook.USUARIO(username),
  reacao INT DEFAULT 0 COMMENT '-1 NÃO CURTIU, 0 NEUTRO E 1 CURTIU',
  idPOST INT NOT NULL COMMENT 'id do post que foi curtido pelo usuário',
  FOREIGN KEY (idPOST)
    REFERENCES birdbook.POST(idPOST),
  CONSTRAINT CURT_ck CHECK (reacao IN (-1,0,1)),
  PRIMARY KEY (username, idPOST));


-- -----------------------------------------------------
-- Table birdbook.ACESSO
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.ACESSO ;

CREATE TABLE IF NOT EXISTS birdbook.ACESSO (
  idACESSO INT NOT NULL AUTO_INCREMENT COMMENT 'id do acesso',
  IP VARCHAR(45) NULL COMMENT 'IP que foi usado para executar a visualização',
  Browser VARCHAR(45) NULL COMMENT 'browser que foi utilizado no acesso em que a visualização aconteceu',
  Aparelho VARCHAR(45) NULL COMMENT 'aparelho utilizado para executar o acesso atrelado à visualização',
  PRIMARY KEY (idACESSO));



-- -----------------------------------------------------
-- Table birdbook.VISUALIZACAO
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.VISUALIZACAO ;

CREATE TABLE IF NOT EXISTS birdbook.VISUALIZACAO (
  idACESSO INT NOT NULL COMMENT 'id do acesso em que a visualização ocorreu',
  FOREIGN KEY (idACESSO)
    REFERENCES birdbook.ACESSO(idACESSO),
  idPOST INT NOT NULL COMMENT 'id do post que foi visualizado',
  FOREIGN KEY (idPOST)
    REFERENCES birdbook.POST(idPOST),
  username VARCHAR(45) NOT NULL COMMENT 'usuário que executou a visualização',
	FOREIGN KEY (username)
    REFERENCES birdbook.USUARIO(username),
  stamp TIMESTAMP(6) NOT NULL COMMENT 'momento em que a visualização aconteceu',
  PRIMARY KEY (idACESSO, idPOST, stamp));



-- -----------------------------------------------------
-- Table birdbook.TAG_USUARIO_POST
-- -----------------------------------------------------
DROP TABLE IF EXISTS birdbook.TAG_USUARIO_POST ;

CREATE TABLE IF NOT EXISTS birdbook.TAG_USUARIO_POST (
  username VARCHAR(45) NOT NULL COMMENT 'usernema do usuário ao qual o post pertence',
  FOREIGN KEY (username)
    REFERENCES birdbook.USUARIO(username),
  idPOST INT NOT NULL COMMENT 'is do post que pertence ao usuário',
  FOREIGN KEY (idPOST)
    REFERENCES birdbook.POST(idPOST),
  PRIMARY KEY (username, idPOST));


USE birdbook;

DELIMITER $$

USE birdbook$$
DROP TRIGGER IF EXISTS birdbook.USUARIO_AFTER_DELETE $$
USE birdbook$$
CREATE DEFINER = CURRENT_USER TRIGGER birdbook.USUARIO_AFTER_DELETE AFTER DELETE ON USUARIO FOR EACH ROW
BEGIN
	DELETE FROM USUARIO_PREFERE_PASSARO
        WHERE USUARIO_PREFERE_PASSARO.username = OLD.username;
END$$


USE birdbook$$
DROP TRIGGER IF EXISTS birdbook.USUARIO_AFTER_DELETE_POST $$
USE birdbook$$
CREATE DEFINER = CURRENT_USER TRIGGER birdbook.USUARIO_AFTER_DELETE_POST AFTER DELETE ON USUARIO FOR EACH ROW
BEGIN
	UPDATE POST
		SET deleta = '1' 
        WHERE POST.username = OLD.username;
END$$


USE birdbook$$
DROP TRIGGER IF EXISTS birdbook.PASSARO_AFTER_DELETE $$
USE birdbook$$
CREATE DEFINER = CURRENT_USER TRIGGER birdbook.PASSARO_AFTER_DELETE AFTER DELETE ON PASSARO FOR EACH ROW
BEGIN
	DELETE FROM USUARIO_PREFERE_PASSARO
        WHERE USUARIO_PREFERE_PASSARO.tag_PASSARO = OLD.tag_PASSARO;
END$$

USE birdbook$$
DROP TRIGGER IF EXISTS birdbook.POST_AFTER_UPDATE $$
USE birdbook$$
CREATE DEFINER = CURRENT_USER TRIGGER birdbook.POST_AFTER_UPDATE AFTER UPDATE ON POST FOR EACH ROW
BEGIN
	IF NEW.deleta = TRUE THEN
		DELETE FROM TAG_PASSARO_POST
			WHERE TAG_PASSARO_POST.idPOST = NEW.idPOST;
		DELETE FROM TAG_USUARIO_POST 
			WHERE TAG_USUARIO_POST.idPOST = NEW.idPOST;
		DELETE FROM VISUALIZACAO 
			WHERE VISUALIZACAO.idPOST = NEW.idPOST;
		DELETE FROM JOINHA 
			WHERE JOINHA.idPOST = NEW.idPOST;
	END IF;
END$$


USE birdbook$$
DROP TRIGGER IF EXISTS birdbook.VISUALIZACAO_AFTER_DELETE $$
USE birdbook$$
CREATE DEFINER = CURRENT_USER TRIGGER birdbook.VISUALIZACAO_AFTER_DELETE AFTER DELETE ON VISUALIZACAO FOR EACH ROW
BEGIN
    DELETE FROM ACESSO 
        WHERE ACESSO.idACESSO = OLD.idACESSO;
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
