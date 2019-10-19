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



-- timestamp_post
ALTER TABLE POST
ADD stamp_post TIMESTAMP DEFAULT current_timestamp NOT NULL COMMENT 'momento em que a publicação do post aconteceu';
CREATE INDEX stamp_post ON POST (stamp_post DESC);

DROP PROCEDURE IF EXISTS foto_passaro;
DELIMITER //
CREATE PROCEDURE foto_passaro()
BEGIN
    SELECT tag_PASSARO, URL_foto FROM TAG_PASSARO_POST 
    INNER JOIN POST ON POST.idPOST = TAG_PASSARO_POST.idPOST;
END //


-- mais pop
DROP PROCEDURE IF EXISTS mais_pop;
DROP TABLE IF EXISTS visu_post;
DELIMITER //
CREATE PROCEDURE mais_pop()
BEGIN
	CREATE TABLE visu_post
		SELECT POST.username, USUARIO.idCIDADE, COUNT(POST.idPOST) AS cnt
		FROM POST
		INNER JOIN VISUALIZACAO ON VISUALIZACAO.idPOST = POST.idPOST
        INNER JOIN USUARIO ON POST.username = USUARIO.username
        GROUP BY username;
        SELECT idCIDADE, MAX(cnt) as m FROM visu_post GROUP BY idCIDADE;
	SELECT B.idCIDADE, B.username, cnt
	FROM (SELECT idCIDADE, MAX(cnt) as m FROM visu_post GROUP BY idCIDADE)
    AS A INNER JOIN visu_post AS B ON A.idCIDADE = B.idCIDADE AND A.m = B.cnt;
    DROP TABLE visu_post;
END//


-- mais visualizador

DROP PROCEDURE IF EXISTS mais_visualizador;

DELIMITER //
CREATE PROCEDURE mais_visualizador()
BEGIN
    SELECT username, COUNT(username) as quantas_visuializacoes FROM VISUALIZACAO
    GROUP BY username
    ORDER BY quantas_visuializacoes DESC
    LIMIT 3;
END//


# orderna

DROP PROCEDURE IF EXISTS ordena_post_usuario;

DELIMITER //
CREATE PROCEDURE ordena_post_usuario(userN VARCHAR(45))
BEGIN
    SELECT * FROM POST WHERE username = userN
    ORDER BY stamp_post DESC;
END//
DELIMITER ;

-- referencia usuario

DROP PROCEDURE IF EXISTS referenciam_usu;

CREATE PROCEDURE referenciam_usu(user_ VARCHAR(45))    
SELECT POST.username
FROM POST
INNER JOIN TAG_USUARIO_POST ON TAG_USUARIO_POST.idPOST = POST.idPOST
WHERE TAG_USUARIO_POST.username = user_;  


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
