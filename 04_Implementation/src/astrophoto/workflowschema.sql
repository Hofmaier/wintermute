CREATE TABLE IF NOT EXISTS projects(
       name text,
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
       imagetype INTEGER,
       duration INTEGER	
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
       adapterID INTEGER,
       telescopeID INTEGER,
       projectID INTEGER
);

