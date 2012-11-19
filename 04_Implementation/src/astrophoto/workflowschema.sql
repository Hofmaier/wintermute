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
       duration INTEGER,	
       project INTEGER
);

CREATE TABLE IF NOT EXISTS shots(
       shotdescription INTEGER
);

CREATE TABLE IF NOT EXISTS imagingfunctions(
       spectralchanneluuid TEXT,
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
       adapterName text,
       telescopeName text
);

