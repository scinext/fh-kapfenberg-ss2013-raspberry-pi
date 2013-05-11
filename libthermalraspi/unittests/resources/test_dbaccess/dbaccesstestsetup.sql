DROP TABLE IF EXISTS "sensors";
DROP TABLE IF EXISTS "measurements";

CREATE  TABLE "main"."sensors" (
	"id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
	"name" VARCHAR NOT NULL  UNIQUE
);

CREATE TABLE "measurements" (
	"sensorid" Integer NOT NULL , 
	"timestamp" DATETIME NOT NULL , 
	"value" FLOAT,
	"errorcode" INTEGER, 
	FOREIGN KEY(sensorid) REFERENCES sensors(id),
	PRIMARY KEY ("sensorid", "timestamp")
);

INSERT INTO sensors (name) VALUES ('ad7414');
INSERT INTO sensors (name) VALUES ('hyt221');
INSERT INTO sensors (name) VALUES ('lm73');
INSERT INTO sensors (name) VALUES ('tc74');

INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='hyt221' LIMIT 1), '2012-12-31 23:57:00',NULL,'Hyt221 IO Error');
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='lm73' LIMIT 1), '2012-12-31 23:57:00',NULL,'Das ist ein Error');
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='lm73' LIMIT 1), '2012-12-31 23:58:00',0.33,NULL);
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='lm73' LIMIT 1), '2012-12-31 23:59:00',31.01,NULL);
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='lm73' LIMIT 1), '2013-01-01 00:00:00',31.02,NULL);
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='lm73' LIMIT 1), '2013-01-01 00:01:00',31.03,NULL);
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='ad7414' LIMIT 1), '2013-01-01 23:58:00',3.33,NULL);
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='ad7414' LIMIT 1), '2013-01-01 23:59:00',3.34,NULL);
INSERT INTO measurements ([sensorid],[timestamp],[value],[errorcode]) VALUES ((SELECT id FROM sensors WHERE name='hyt221' LIMIT 1), '2012-01-01 23:57:00',100.0,NULL);
