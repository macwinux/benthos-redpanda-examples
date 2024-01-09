CREATE  KEYSPACE foo WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
CREATE TABLE foo.bar("id" text primary key, "name"  text, "gooeyness" double, "bouncing" boolean  );
