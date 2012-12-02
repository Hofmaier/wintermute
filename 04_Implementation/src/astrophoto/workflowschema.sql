CREATE TABLE IF NOT EXISTS projects(
       name text,
       opticalSystemID INTEGER,
       cameraconfiguration INTEGER
);

CREATE TABLE IF NOT EXISTS cameraconfigurations(
      name text,
      interface text
);

CREATE TABLE IF NOT EXISTS imagetypes(
       identifier text
);

CREATE TABLE IF NOT EXISTS shotdescriptions(
       imagetype TEXT,
       duration FLOAT,	
       project INTEGER,
       kind TEXT
);

CREATE TABLE IF NOT EXISTS images(
       shotdescription INTEGER,
       filename TEXT
);

CREATE TABLE IF NOT EXISTS imagingfunctions(
       spectralchanneluuid TEXT,
       spectraltag TEXT,
       spatialfunction TEXT,
       imagetype TEXT,
       cameraconfiguration INTEGER 
);


CREATE TABLE IF NOT EXISTS adapters(
       name text
);

CREATE TABLE IF NOT EXISTS telescopes(
       name text
);

CREATE TABLE IF NOT EXISTS opticSystems(
       adapterRowId INTEGER,
       telescopeRowId INTEGER
);

