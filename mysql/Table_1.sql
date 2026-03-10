create database PITANGHSU;
USE PITANGHSU;
CREATE TABLE STUDENT (
ROLL INT auto_increment primary KEY,
NAME varchar(50),
CLASS VARCHAR(50),
SECTION VARCHAR(50),
MARKS INT
);
insert INTO STUDENT (NAME, CLASS, SECTION, MARKS)
values
('AMIT', 'XII', 'A', 7),
('RIYA', 'XII', 'A', 85),
('SUMAN', 'XII', 'B', 67),
('NEHA', 'XII', 'B', 92),
('RAHUL', 'XII', 'C', 54),
('POOJA', 'XII', 'A', 88),
('KUNAL', 'XII', 'C', 73),
('ANITA', 'XII', 'B', 81),
('VIKAS', 'XII', 'A', 69),
('MEENA', 'XII', 'C', 95);
