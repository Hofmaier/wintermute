CREATE TABLE IF NOT EXISTS projects(
       name text,
       PRIMARY KEY(name)
);

CREATE TABLE IF NOT EXISTS cameraconfigurations(
       name text,
       project INTEGER,
       interface text
);

CREATE TABLE IF NOT EXISTS imagetypes(
       identifier text
);

CREATE TABLE IF NOT EXISTS shotdescriptions(
       imagetype INTEGER,
       duration INTEGER	
);

CREATE TABLE IF NOT EXISTS adapters(
       name text
);

CREATE TABLE IF NOT EXISTS telescopes(
       name text
);

CREATE TABLE IF NOT EXISTS opticSystems(
       adapterID INTEGER,
       telescopeID INTEGER,
       projectID INTEGER
);
