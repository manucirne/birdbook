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

DELIMITER $$
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