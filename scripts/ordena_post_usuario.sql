USE birdbook;

DROP PROCEDURE IF EXISTS ordena_post_usuario;

DELIMITER //
CREATE PROCEDURE ordena_post_usuario(userN VARCHAR(45))
BEGIN
    SELECT * FROM POST WHERE username = userN
    ORDER BY stamp_post DESC;
END//
DELIMITER ;