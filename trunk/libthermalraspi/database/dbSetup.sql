
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