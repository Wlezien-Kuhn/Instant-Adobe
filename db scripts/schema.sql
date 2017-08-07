create database instant_adobe_data;

create table templates(

	Title varchar(50) not null unique,
	Poster varchar(50),
	Aep varchar(50) not null,
	Mov varchar(50) not null,
	UUID char(16) not null unique

);