-- sdfsd
ALTER TABLE second_table ADD average INT;
INSERT INTO second_table (average) 
SELECT SUM(score) * 1.0 / COUNT(*);
