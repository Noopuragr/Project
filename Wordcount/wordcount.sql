DROP DATABASE IF EXISTS documents CASCADE;

CREATE DATABASE documents;

USE documents;

CREATE TABLE docs(words string);

LOAD DATA LOCAL INPATH '/home/cloudera/Desktop/Hive' INTO TABLE docs;

CREATE TABLE word_count AS
SELECT word, count(*) AS count FROM
(SELECT explode(split(words, '\\W+')) AS word FROM docs) w
GROUP BY word;

SELECT * FROM word_count limit 100;
