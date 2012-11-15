CREATE TABLE IF NOT EXISTS projects(
       name text,
       PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS cameraconfigurations(
       name text,
       project INTEGER,
       interface text,
       PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS imagetypes(
       identifier text
);

CREATE TABLE IF NOT EXISTS shotdescriptions(
       imagetype INTEGER,
       duration INTEGER	
);
