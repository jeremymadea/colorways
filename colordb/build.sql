CREATE TABLE colors (
    topset TEXT NOT NULL,
    subset TEXT, 
    name TEXT,
    hex TEXT,
    valid INTEGER,
    notes TEXT
);

.mode csv 
.separator |
.import csv/crayola_standard.csv colors
.import csv/crayola_fluorescent.csv colors
.import csv/crayola_silver_swirls.csv colors
.import csv/w3-colors.csv colors
