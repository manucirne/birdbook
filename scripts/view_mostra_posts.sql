USE birdbook;

DROP VIEW IF EXISTS exibe_posts;

CREATE VIEW exibe_posts AS
	SELECT username, titulo, texto, stamp_post FROM POST
    ORDER BY stamp_post DESC;