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
.import csv/xkcd.csv colors
.import csv/x11_old.csv colors
.import csv/x11_1.1.csv colors
.import csv/x11_1.2.csv colors
.import csv/xorg.csv colors
.import csv/aus.csv colors
.import csv/bs381.csv colors
.import csv/bs4800.csv colors
