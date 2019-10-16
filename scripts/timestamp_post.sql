ALTER TABLE POST
ADD stamp_post TIMESTAMP DEFAULT current_timestamp NOT NULL COMMENT 'momento em que a publicação do post aconteceu';
CREATE INDEX stamp_post ON POST (stamp_post DESC);