USE birdbook;

DROP PROCEDURE IF EXISTS foto_passaro;

DELIMITER //
CREATE PROCEDURE foto_passaro()
BEGIN
    SELECT tag_PASSARO, URL_foto FROM TAG_PASSARO_POST 
    INNER JOIN POST ON POST.idPOST = TAG_PASSARO_POST.idPOST;
END//