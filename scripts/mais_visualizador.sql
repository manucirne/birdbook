USE birdbook;

DROP PROCEDURE IF EXISTS mais_visualizador;

DELIMITER //
CREATE PROCEDURE mais_visualizador()
BEGIN
    SELECT username, COUNT(username) as quantas_visuializacoes FROM VISUALIZACAO
    GROUP BY username
    ORDER BY quantas_visuializacoes DESC
    LIMIT 3;
END//
DELIMITER ;