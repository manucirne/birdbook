DROP VIEW IF EXISTS exibe_posts;

CREATE VIEW exibe_posts AS
	SELECT username, titulo, texto, stamp_post FROM POST
    ORDER BY time_stamp DESC;