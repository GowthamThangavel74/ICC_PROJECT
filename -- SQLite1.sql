-- SQLite
CREATE TABLE ICC (
 Job_id INTEGER PRIMARY KEY,
 Opening_Job TEXT NOT NULL,
 Job_Des TEXT NOT NULL,
 Aplication_counts TEXT NOT NULL,
 Aplication_Viewed TEXT NOT NULL
);

SELECT * FROM ICC where Job_id='1006'

SELECT * FROM ICC2 where Job_id='1006'

SELECT * FROM ICC2


INSERT INTO ICC (Job_id, Opening_Job, Job_Des, Aplication_counts, Aplication_Viewed) VALUES (1002, 'Python', 'Developer', 15, 9);
INSERT INTO ICC (Job_id, Opening_Job, Job_Des, Aplication_counts, Aplication_Viewed) VALUES (1003, 'Sr.Python', 'Developer', 50, 25);
INSERT INTO ICC (Job_id, Opening_Job, Job_Des, Aplication_counts, Aplication_Viewed) VALUES (1004, 'Sof_Developr', 'Developer', 100, 77);
INSERT INTO ICC (Job_id, Opening_Job, Job_Des, Aplication_counts, Aplication_Viewed) VALUES (1005, 'Sr.Soft_developer', 'Developer', 88, 69);

SELECT Job_id FROM ICC WHERE Job_id='1001'

INSERT INTO ICC (Job_id, Opening_Job, Job_Des, Aplication_counts, Aplication_Viewed) VALUES (1006, '.Net', 'Developer', 19, 19);

UPDATE ICC set Opening_Job='Softwar_Developer_1' where Job_id='1100'

DELETE FROM ICC where Job_id='1006'

