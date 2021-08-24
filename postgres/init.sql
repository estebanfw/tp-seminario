DROP TABLE IF EXISTS btc;

CREATE TABLE btc (
	datetime 	timestamp with time zone primary key,
    coin 		varchar(255) NOT NULL,
    price 		double precision
);

