CREATE TABLE colors (
    topset TEXT NOT NULL,
    subset TEXT, 
    name TEXT,
    hex TEXT,
    valid INTEGER,
    notes TEXT
);

-- Load the data. 
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
.import csv/nbc-iscc.csv colors
.import csv/fs595c.csv colors
.import csv/fs595_ana.csv colors
.import csv/fs595_camo.csv colors
.import csv/fs595_highway.csv colors
.import csv/fs595_safety.csv colors
.import csv/ncs.csv colors
.import csv/resene.csv colors

-- uppercase the hex column to ensure consistency. 
UPDATE colors SET hex = UPPER(hex);
