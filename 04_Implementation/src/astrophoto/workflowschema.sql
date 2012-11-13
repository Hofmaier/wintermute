CREATE TABLE IF NOT EXISTS projects(
       name text
);

CREATE TABLE IF NOT EXISTS cameraconfigurations(
       name text,
       project INTEGER,
       interface text
);
