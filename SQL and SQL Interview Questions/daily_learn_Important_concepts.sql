--Database
We can store data inside the table in properway


--DBMS
Its an software for manages the Databases


--DataModels
its mainly four types
1)Hirarechy model
2)Network model
3)Entity-Relational model
4)Relational model (Its popular)

--RDBMS
Its software mainly used for relational types of data.

MySQL:
Developed by Oracle Corporation.
Open-source and widely used for web applications.
Supports SQL (Structured Query Language).

Oracle Database:
Developed by Oracle Corporation.
A powerful and widely used commercial RDBMS.
Known for its scalability and advanced features.

PostgreSQL:
Open-source RDBMS known for its extensibility and standards compliance.
Supports advanced data types and features.


--NRBMS
Its software mainly used for non-relational types of data
Non-Relational Database Management Systems (NRDBMS) are also known as NoSQL databases.
Unlike RDBMS, NoSQL databases do not strictly adhere to the traditional relational model
Designed to handle unstructured or semi-structured data.

Examples
MongoDB:
A document-oriented NoSQL database.
Stores data in flexible, JSON-like BSON documents.
Widely used for scalable and high-performance applications.


Amazon DynamoDB:
A fully managed NoSQL database service provided by Amazon Web Services (AWS).
Designed for high-performance, low-latency applications with automatic scaling.

Cassandra:
A distributed NoSQL database designed for handling large amounts of data across multiple commodity servers.
Known for its high availability and fault tolerance.


--One-to-One Relationship:
Retrieve a person and their passport information:

SELECT Person.FirstName, Person.LastName, Passport.PassportID, Passport.Country
FROM Person
JOIN Passport ON Person.PersonID = Passport.PersonID;

--One-to-Many Relationship:
Retrieve employees and their respective departments:

SELECT Employee.EmployeeID, Employee.Salary, Department.DepartmentName
FROM Employee
JOIN Department ON Employee.DepartmentID = Department.DepartmentID;

--Many-to-Many Relationship:
Retrieve students and the courses they are enrolled in:
SELECT Student.StudentName, Course.CourseName
FROM Student
JOIN StudentCourse ON Student.StudentID = StudentCourse.StudentID
JOIN Course ON StudentCourse.CourseID = Course.CourseID;

--select
for retrivieng the data from databases.
select * from customers;
select customer_id from customers;
select customer_name,customer_id from customers;

--distinct
for removing duplicate records from the table.
select distinct (*) from customers;
select distinct customer_id from customers;
select distinct customer_name,customer_id from customers;

--SQL Case not sensitive
sql is not a case sensitive

--Semicolon
Its optional for some RDBMS SOME RDBMS need the semicolon

--where
Its maily used for apply the filter conditions
Its used with select and update and delete commands
select * from customer_id from customers where city = 'London';
select customer_name,customer_id from customers where customer_id = 9;

--Where clause with Relational Operators
Using Relational operators we can filter the using one condition
--Equal operator(=)
select * from products where price = 40;
--Greater Than Operator(>)
select * from products where price > 40;
--Less Than Operator(<)
select * from products where price < 40;
--Greater Than or Equal to(>=)
select * from products where price >= 40;
--Less Than or Equal to(<=)
select * from products where price <= 40;
--Not Equal to(<>)
select * from products where price <> 40;

--Logical operators

Using Logical operators we can filter the using multiple conditions

--AND
select * from customers where country = 'Mexico' AND customer_id > 3;
--OR
select * from customers where country = 'Mexico' OR customer_id > 3 OR contactName <> 'Lingababu';
--NOT
select * from customers where NOT Country = 'Germeny'

--Between operator
Between Operator is used to filetr the records in the specified range

select * from products where price Between 10 AND 20;
select * from products where price >=10 AND Price <=20;
Between 50 to 60 50,51,..............60

select * from products where price NOT Between 10 AND 20;
select * from products where price < 10 AND Price < 20;
Not Between 1,2,3........49  61,62........100


