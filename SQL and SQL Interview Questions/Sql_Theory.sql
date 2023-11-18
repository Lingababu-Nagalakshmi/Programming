SQL BASICS
QL Introduction
SQL Getting Started
SQL Syntax
--SQL Create Database--

Create DATABASE Guggilapu

--SQL Create Table--
Create Table Lingababu (

fname,varchar(255), UNIQUE,
lname,varchar(255), UNIQUE)

--SQL Constraints--
1)UNIQUE
2)NOT NULL
3)DEFAULT

--SQL Insert--
INSERT Lingababu (fname,)

--SQL Select--
1)select * from Table
2)select COLUMNS from Table


--SQL Where is used to fetch the particular data from Database--
select * from table Where id = 30
select * from table where city = 'hyderabad'


--SQL AND & OR is are for bitwise operators--
select * from table where salary BETWEEN 2000 and 3000;
select * from table where salary between 2000 or 3000; 

--SQL IN & Between--


--SQL Order By   this is we can use along with select statement--
select * from table ORDER BY salary;

 
--SQL Top/Limit--


--SQL Distinct is used to remove the duplicates records--
select Distinct Empid from table

--SQL Update--
--SQL Delete is used to remove the duplicates records from the table-- 

--SQL Truncate Table--
--SQL Drop--
--SQL JOIN-- is used to join the tables based on matched columns

--SQL Joining Tables
--SQL Inner Join
select t1.emp_name,t1.emp_age,t2.dept_id,t2.dept_name
from employees as t1 INNER JOIN department as t2
on t1.dept_id = t2.dept_id OREDR BY emp_id


--SQL Left Join--
select t1.emp_name,t1.emp_age,t2.dept_id,t2.dept_name
from employees as t1 LEFTJOIN department as t2
on t1.dept_id = t2.dept_id ORDER BY emp_id

--SQL Right Join
select t1.emp_name,t1.emp_age,t2.dept_id,t2.dept_name
from employees as t1 RIGHT JOIN department as t2
on t1.dept_id = t2.dept_id ORDER BY emp_id

--SQL Full Join--
select t1.emp_name,t1.emp_age,t2.dept_id,t2.dept_name
from employees as t1 FULLJOIN department as t2
on t1.dept_id = t2.dept_id ORDER BY emp_id

--SQL Cross Join--
select t1.emp_name,t1.emp_age,t2.dept_id,t2.dept_name
from employees as t1 RIGHT JOIN department as t2
on t1.dept_id = t2.dept_id ORDER BY emp_id

--SQL ADVANCED
--SQL Union
select frist_name , last_name from employees
UNION 
select frist_name,last_name from customers;

--SQL Unionall
select frist_name , last_name from employees
Unionall 
select frist_name,last_name from customers;


--SQL Like
WHERE name LIKE 'Da%'	Find names beginning with Da	David, Davidson
WHERE name LIKE '%th'	Find names ending with th	Elizabeth, Smith

select * from employees 
WHERE emp_name LIKE 'S%';


--SQL Alter Table 
--It will modify the existing table

ALTER Table 1)adding   column          [ALTER TABLE Employee ADD Emp_area VARCHAR(20);]
			2)changing column           ALTER TABLE  
			3)deleting column          [ALTER TABLE table_name DROP COLUMN column_name;]
			4)CHANGING Column Position [ALTER TABLE table_name MODIFY Emp_age VARCHAR(20) AFTER Emp_salary;]
			5)Adding Constraints       [ALTER table_name ADD UNIQUE (column_name)]
			                           [ALTER table_name ADD PRIMARY KEY (column_name)]
			6)Changing datatype of column:
                                       [ALTER TABLE table_name ALTER COLUMN column_name new_data_type]			
			7)Renaming the table:      [ALTER TABLE current_table RENAME new_column_name;]					 
--SQL Aliases
SELECT t1.emp_name,t1.emp_age,t2.dept_name,t2.dept_id
FROM Employee as t1 INNER JOIN department as t2
ON t1.dept_id = t2.dept_id OREDR BY emp_id

--SQL Group By

-- The GROUP BY clause must appear after the FROM and WHERE clauses, and before the ORDER BY in a SQL SELECT statement.--
SELECT t1.dept_name, count(t2.emp_id) AS total_employee
from department as t1 LEFT JOIN employee as t2
ON t1.dept_id = t2.dept_id
GROUP BY t1.dept_name;

--SQL Having

SELECT t1.dept_name, count(t2.emp_id) AS total_employees
FROM departments AS t1 LEFT JOIN employees AS t2
ON t1.dept_id = t2.dept_id
GROUP BY t1.dept_name
HAVING total_employees = 0;

--SQL Create View

--CREATE VIEW view_name AS select_statement--

CREATE VIEW emp_dept_view AS
SELECT t1.emp_name,t1.emp_age,t2.dept_name,t2.dept_id
FROM Employee as t1 INNER JOIN department as t2
ON t1.dept_id = t2.dept_id OREDR BY emp_id

SELECT * FROM emp_dept_view;
SQL Create Index

CREATE INDEX index_name ON table_name (column_name);

--SQL Dates and Times

--DATE	YYYY-MM-DD	1000-01-01 to 9999-12-31--
--TIME	HH:MM:SS or HHH:MM:SS	-838:59:59 to 838:59:59--
--DATETIME	YYYY-MM-DD HH:MM:SS	1000-01-01 00:00:00 to 9999-12-31 23:59:59--
--TIMESTAMP	YYYY-MM-DD HH:MM:SS	1970-01-01 00:00:00 to 2037-12-31 23:59:59--
--YEAR	YYYY	1901 to 2155--

--Syntax for MySQL Database--
INSERT INTO users (name, birth_date, created_at)
VALUES ('Lingababu', '1992-04-16' , NOW())


SQL Cloning Tables
SQL Temporary Tables

--creating temporary table--
CREATE TEMPORARY TABLE persons SELECT * FROM persons;

--Dropping a temporary table--

DROP Temporary TABLE persons;

SQL Subqueries

select * from customers 

where cust_id IN (SELECT Distinct cust_id From orders

where order_value > 5000);
SQL Injection

--SQL injection is an attack wherein an attacker can inject or execute malicious SQL code via the input data from the browser to the application server, such as web-form input.--

--How SQL Injection Works
Consider the following SQL statement which is a simple example of authenticating a user with a username and password in a web application.

SELECT * FROM users WHERE username='username_val' AND password='password_val';


SQL REFERENCE
SQL Data Types

Binary data type	Nonbinary data type	Maximum length
BINARY	CHAR	255
VARBINARY	VARCHAR	65,535
TINYBLOB	TINYTEXT	255
BLOB	TEXT	65,535
MEDIUMBLOB	MEDIUMTEXT	16,777,215
LONGBLOB	LONGTEXT	4,294,967,295

Data Type	Range (Signed)	Range (Unsigned)
TINYINT	-128 to 127	0 to 255
SMALLINT	-32768 to 32767	0 to 65535
MEDIUMINT	-8388608 to 8388607	0 to 16777215
INT	-2147483648 to 2147483647	0 to 4294967295
BIGINT	-9223372036854775808 to 9223372036854775807	0 to 18446744073709551615


--SQL Functions
--CASE condition with ELSE clause in SQL


SELECT customer_id,first_name,
CASE
	WHEN country = 'USA' THEN 'United States of America'
	WHEN country = 'UK'  THEN 'United Kingdom'
	ELSE 'Unknown Country'
	
END AS country_name
FROM Customers;


SELECT customer_id,frist_name
CASE
	WHEN age >=18 THEN 'Allowed'
END AS can_vote

FROM Customers;
