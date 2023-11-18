CREATE DATABASE kadiyadda

CREATE TABLE LINGABABU (

ID INTEGER,
LASTNAME VARCHAR(255),
FRISTNAME VARCHAR(255),
ADDRESS VARCHAR(255),
CITY   VARCHAR(255));
 

INSERT INTO LINGABABU(ID,LASTNAME,FRISTNAME,ADDRESS,CITY)
VALUES (1,'GUGGILAPU','LINGABABU','KADIYADDA','TADEPALLIGUDEM')


 
ALTER TABLE LINGABABU  --add the column--

ADD EMAIL VARCHAR(255)



ALTER TABLE LINGABABU      --remove the column--

DROP COLUMN EMAIL;


ALTER TABLE LINGABABU      -- for rename the column--

RENAME COLUMN LINGABABU to lingababu;


ALTER TABLE LINGABABU       -- for change the column datatype--

ALTER COLUMN DATATYPE;


UPDATE LINGABABU             --for update the Data--

SET CONTACT NAME ='ALREAD SCHMIDT' CITY ='GERMANY' WHERE CUSTOMER ID =1


SELECT SALARY FROM EMPLOYEE ORDER BY SALARY DESC LIMIT 2-1,1;

SELECT SALARY FROM EMPLOYEE ORDER BY SALARY DESC LIMIT 3-1,1;

SELECT MAX(SALARY ) FROM EMPLOYEE

SELECT CONCAT('FRISTNAME','','LASTNAME') AS 'FULL NAME' FROM EMPLOYEE 

-- where we are using the clauses in sql--
SELECT: selects the columns from the database to output to the result.
FROM: lists the tables to be used in the query.
WHERE: filters individual records.
GROUP BY: groups the records based on the column(s) specified.
HAVING: filters the groups defined by GROUP BY.
ORDER BY: sorts the output records by the column(s) specified.



-- deleting duplicate records from the table--
DELETE FROM TABLE WHERE ID IN (    
SELECT 
ID, COUNT(ID)
FROM TABLE 
GROUP BY ID
HAVING 
COUNT(ID)>1);

-- how we can get the only duplicate records from the table--
-- duplicates in SQL by using the GROUP BY and HAVING clauses.--
SELECT OrderID, COUNT(OrderID)
FROM Orders
GROUP BY OrderID
HAVING COUNT(OrderID) > 1

-- sub query--
--writing a query inside a query is a subquery--

select frist_name last_name from employee where Officecode in (select Officecode in office where Country = 'usa');


SELECT UPPER(EMPFNAME) as EmpName from EMPLOYEE

SELECT COUNT(*) FROM EMPLOYEE WHERE DEPARTMENT = 'HR'

SELECT SUBSTRING(EMPLASTNAME,1,4) FROM EMPLOYEE

SELECT * INTO NEWTABLE FROM EMPLOYEE WHERE 1 = 0;

SELECT * FROM EMPLOYEE WHERE SALARY BETWEEN '5000' AND '10000';

SELECT * FROM EMPLOYEE WHERE EMPFNAME LIKE '%S';

--The percent sign (%) represents zero, one, or multiple characters--
--The underscore sign (_) represents one, single character--

SELECT * FROM EMPLOYEE ORDERBY EMPFNAME DESC DEPARTMENT ASC ;

SELECT * FROM EMPLOYEE WHERE EMPFNAME LIKE '___a%';



-- GET THE EVEN NUMBER OF RECORDS FROM THE TABLE--
SELECT * FROM table_name where MOD(COLUMN_NAME,2) = 0;

-- GET THE ODD NUMBER OF RECORDS FROM THE TABLE--
SELECT * FROM table_name where MOD(COLUMN_NAME,2) = 1;


SELECT Orders.OrdersID, Customers.CustomerName, Orders.OrderDate
from Orders
INNER JOIN Customers 
on Customers.CustomerID = Orders.OrderID


SELECT Customers.CustomerName,Orders.OredrID
FROM Customers
LEFT JOIN Orders 
ON CUSTOMERS.CUSTOMERID = ORDERS.ORDERID;


SELECT EmpId , FullName From EmployeeDetails WHERE ManagerId = 986;

SELECT DISTINCT(Project) FROM EmployeeSalary;

SELECT COUNT(*) FROM EmployeeSalary WHERE Project = 'P1';

SELECT Max(Salary),Min(Salary),Avg(Salary) FROM EmployeeSalary;

SELECT EmpId, Salary FROM EmployeeSalary WHERE Salary BETWEEN 9000 AND 15000;

SELECT EMPID, city, M anagerId FROM EmployeeDetails WHERE City = 'Toronto' AND ManagerId = '321'

SELECT EMPID,CITY, ManagerId FROM EmployeeDetails WHERE City = 'California' OR ManagerId = '321';

SELECT EMPID FROM EmployeeSalar WHERE NOT Project = 'P1'; 

--records not in with the names SANJAY and SANJU--

SELECT * FROM EMPLOYEE WHERE EMPLOYEE NOT IN ('SANJAY','SANJU');

--BOTH ARE WILL APPLICABLE FOR NOT IN EXAMPLE --

SELECT EMPID FROM EmployeeSalary WHERE Project <> 'P1';

--Write an SQL query to display the total salary of each employee adding the Salary with Variable value.--

SELECT EmpID, Salary+Variable as TotalSalary From EmployeeSalary;

-- SQL query to fetch the employees whose name begins with any two characters, followed by a text “hn” and ends with any sequence of characters.--

SELECT FullName FROM EmployeeDetails WHERE FullName LIKE `__hn%`;

--SQL query to fetch the EmpIds that are present in both the tables –  ‘EmployeeDetails’ and ‘EmployeeSalary.--

SELECT EmpId FROM EmployeeDetails Where EmpID IN (SELECT EmpID FROM EmployeeSalary);


--Write a query to fetch employee names and salary records. Display the employee details even if the salary record is not present for the employee.--

SELECT E.FULLNAME, S.SALARY
FROM EmployeeDetails E 
LEFT JOIN EmployeeSalary S 
ON E.EmpId = S.EmpId 


--Write a SQL Query to add the Three Tables --

SELECT COLUMN1 ,COLUMN2

FROM TableA

JOIN TableB ON TableA.COLUMN3 = TableB.COLUMN3
JOIN TableC ON TableA.COLUMN4 = TableC.COLUMN4;



--Write an SQL query to fetch all the Employees who are also managers from the EmployeeDetails table--

SELECT DISTINCT E.FullName

FROM EmployeeDetails E 

INNER JOIN EmployeeDetails M 
 
ON E.EMPID = M.ManagerId;



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




























