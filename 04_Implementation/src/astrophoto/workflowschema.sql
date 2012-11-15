CREATE TABLE IF NOT EXISTS projects(
       name text
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

CREATE TABLE IF NOT EXISTS imagingfunctions(
       spectralchanneluuid text,
       spatialfunction text
);

