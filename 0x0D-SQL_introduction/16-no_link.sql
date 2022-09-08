--list all records of the second_table of the database hbtn_0c_0
-- rows with no name value are not listed and records are in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
