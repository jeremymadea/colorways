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
.import csv/crayola_multicultural.csv colors
.import csv/crayola_magic_scent.csv colors
.import csv/crayola_gem_tones.csv colors
.import csv/crayola_changeables.csv colors
.import csv/crayola_color_n_smell.csv colors
.import csv/crayola_pearl_brite.csv colors
.import csv/crayola_construction_paper.csv colors
.import csv/crayola_metallic_fx.csv colors
.import csv/crayola_pearl.csv colors
.import csv/crayola_neon.csv colors
.import csv/crayola_colors_of_the_world.csv colors
.import csv/crayola_silly_scents.csv colors
.import csv/crayola_100bn.csv colors
.import csv/crayola_heads_n_tails.csv colors
.import csv/crayola_mini_twistables.csv colors
.import csv/ral.csv colors
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
.import csv/encycolorpedia.csv colors
.import csv/sherwin_williams.csv colors
.import csv/css3_colors.csv colors


-- uppercase the hex column to ensure consistency. 
UPDATE colors SET hex = UPPER(hex);

-- lowercase css3 names (TODO just fix the csv.) 
UPDATE colors SET name = LOWER(name) WHERE topset='CSS3';

-- uppercase the RAL topset name. (TODO fix the csv.)
UPDATE colors SET topset = UPPER(topset) WHERE topset='ral';
