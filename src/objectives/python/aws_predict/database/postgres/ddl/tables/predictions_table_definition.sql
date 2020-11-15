-- public.predictions definition

-- Drop table

-- DROP TABLE public.predictions;

CREATE TABLE public.predictions (
	id serial NOT NULL,
	latitude numeric NULL,
	longitude numeric NULL,
	discovery_date numeric NULL,
	fire_size numeric NULL,
	state_cat int2 NULL,
	owner_descr_cat int2 NULL,
	discovery_day_of_week_cat int2 NULL,
	stat_cause_descr varchar(200) NULL,
	max_probability numeric NULL
);