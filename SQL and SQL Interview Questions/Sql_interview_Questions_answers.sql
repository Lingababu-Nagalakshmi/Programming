SQL QUERIES
-----------

1) Display the details of all employees
    SQL>Select * from emp;

2) Display the depart information from department table
    SQL>select * from dept;

3) Display the name and job for all the employees
    SQL>select ename,job from emp;

4) Display the name and salary  for all the employees
    SQL>select ename,sal from emp;

5) Display the employee no and totalsalary  for all the employees
    SQL>select empno,ename,sal,comm, sal+nvl(comm,0) as"total  salary" from 
    emp

6) Display the employee name and annual salary for all employees.
    SQL>select ename, 12*(sal+nvl(comm,0)) as "annual Sal" from emp

7) Display the names of all the employees who are working in depart number 10.
    SQL>select emame from emp where deptno=10;

8) Display the names of all the employees who are working as clerks and 
   drawing a salary more than 3000.
   SQL>select ename from emp where job='CLERK' and sal>3000;

9) Display the employee number and name  who are earning comm.
   SQL>select empno,ename from emp where comm is not null;

10) Display the employee number and name  who do not earn any comm.
SQL>select empno,ename from emp where comm is null;

11) Display the names of employees who are working as clerks,salesman or 
analyst and drawing a salary more than 3000.
SQL>select ename  from emp where job='CLERK' OR JOB='SALESMAN' 
          OR JOB='ANALYST' AND SAL>3000;

12) Display the names of the employees who are working in the company for 
the past 5 years;
SQL>select ename  from emp where to_char(sysdate,'YYYY')-to_char(hiredate,'YYYY')>=5;

13) Display the list of employees who have joined the company before 
30-JUN-90 or after 31-DEC-90.
a)select ename from emp where hiredate < '30-JUN-1990' or hiredate > 
'31-DEC-90';

14) Display current Date.
SQL>select sysdate from dual;

15) Display the list of all users in your database(use catalog table).
SQL>select username from all_users;

16) Display the names of all tables from current user;
SQL>select tname from tab;

17) Display the name of the current user.
SQL>show user

18) Display the names of employees working in depart number 10 or 20 or 40 
or employees working as
CLERKS,SALESMAN or ANALYST.
SQL>select ename from emp where deptno in(10,20,40) or job 
in('CLERKS','SALESMAN','ANALYST');

19) Display the names of employees whose name starts with alaphabet S.
SQL>select ename from emp where ename like 'S%';

20) Display the Employee names for employees whose name ends with alaphabet S.
SQL>select ename from emp where ename like '%S';

21) Display the names of employees whose names have second alphabet A in 
their names.
SQL>select ename from emp where ename like '_A%';

22) select the names of the employee whose names is exactly five characters 
in length.
SQL>select ename from emp where length(ename)=5;

23) Display the names of the employee who are not working as MANAGERS.
SQL>select ename from emp where job not in('MANAGER');

24) Display the names of the employee who are not working as SALESMAN OR 
CLERK OR ANALYST.
SQL>select ename from emp where job not 
in('SALESMAN','CLERK','ANALYST');

25) Display all rows from emp table.The system should wait after every 
screen full of informaction.
SQL>set pause on 

26) Display the total number of employee working in the company.
SQL>select count(*) from emp;

27) Display the total salary beiging paid to all employees.
SQL>select sum(sal) from emp;

28) Display the maximum salary from emp table.
SQL>select max(sal) from emp;

29) Display the minimum salary from emp table.
SQL>select min(sal) from emp;

30) Display the average salary from emp table.
SQL>select avg(sal) from emp;

31) Display the maximum salary being paid to CLERK.
SQL>select max(sal) from emp where job='CLERK';

32) Display the maximum salary being paid to depart number 20.
SQL>select max(sal) from emp where deptno=20;

33) Display the minimum salary being paid to any SALESMAN.
SQL>select min(sal) from emp where job='SALESMAN';

34) Display the average salary drawn by MANAGERS.
SQL>select avg(sal) from emp where job='MANAGER';

35) Display the total salary drawn by ANALYST working in depart number 40.
SQL>select sum(sal) from emp where job='ANALYST' and deptno=40;

36) Display the names of the employee in order of salary i.e the name of 
the employee earning lowest salary    should salary appear first.
SQL>select ename from emp order by sal;

37) Display the names of the employee in descending order of salary.
a)select ename from emp order by sal desc;

38) Display the names of the employee in order of employee name.
a)select ename from emp order by ename;

39) Display empno,ename,deptno,sal sort the output first base on name and 
within name by deptno and with in deptno by sal.
SQL>select empno,ename,deptno,sal from emp order by

40) Display the name of the employee along with their annual salary(sal*12).The name of the employee earning highest annual salary should apper first.
SQL>select ename,sal*12 from emp order by sal desc;

41) Display name,salary,hra,pf,da,total salary for each employee. The 
output should be in the order of total salary,hra 15% of salary,da 10% of salary,pf 5% 
salary,total salary will be(salary+hra+da)-pf.
SQL>select ename,sal,sal/100*15 as hra,sal/100*5 as pf,sal/100*10 as 
da, sal+sal/100*15+sal/100*10-sal/100*5 as total from emp; 

42) Display depart numbers and total number of employees working in each 
department.
SQL>select deptno,count(deptno)from emp group by deptno;

43) Display the various jobs and total number of employees within each job 
group.
SQL>select job,count(job)from emp group by job;

44) Display the depart numbers and total salary for each department.
SQL>select deptno,sum(sal) from emp group by deptno;


45) Display the depart numbers and max salary for each department.
SQL>select deptno,max(sal) from emp group by deptno;

46) Display the various jobs and total salary for each job
SQL>select job,sum(sal) from emp group by job;

47) Display the various jobs and total salary for each job
SQL>select job,min(sal) from emp group by job;

48) Display the depart numbers with more than three employees in each dept.
SQL>select deptno,count(deptno) from emp group by deptno having 
count(*)>3;

49) Display the various jobs along with total salary for each of the jobs 
where total salary is greater than 40000.
SQL>select job,sum(sal) from emp group by job having sum(sal)>40000;

50) Display the various jobs along with total number of employees in each 
job.The output should contain only those  jobs with more than three employees.
SQL>select job,count(empno) from emp group by job having count(job)>3

51) Display the name of the empployee who earns highest salary.
SQL>select ename from emp where sal=(select max(sal) from emp);

52) Display the employee number and name for employee working as clerk and 
earning highest salary among clerks.
SQL>select empno,ename from emp where where job='CLERK'
           and sal=(select max(sal) from emp  where job='CLERK');

53) Display the names of salesman who earns a salary more than the highest 
salary of any clerk.
SQL>select ename,sal from emp where job='SALESMAN' and sal>(select 
max(sal) from emp
 where job='CLERK');

54) Display the names of clerks who earn a salary more than the lowest 
salary of any salesman.
SQL>select ename from emp where job='CLERK' and sal>(select min(sal) 
from emp
             where job='SALESMAN');

Display the names of employees who earn a salary more than that of 
Jones or that of salary grether than   that of scott.
SQL>select ename,sal from emp where sal>
(select sal from emp where ename='JONES')and sal> (select sal from emp 
where ename='SCOTT');

55) Display the names of the employees who earn highest salary in their 
respective departments.
SQL>select ename,sal,deptno from emp where sal in(select max(sal) from 
emp group by deptno);

56) Display the names of the employees who earn highest salaries in their 
respective job groups.
SQL>select ename,sal,job from emp where sal in(select max(sal) from emp 
group by job)

57) Display the employee names who are working in accounting department.
SQL>select ename from emp where deptno=(select deptno from dept where 
dname='ACCOUNTING')

58) Display the employee names who are working in Chicago.
SQL>select ename from emp where deptno=(select deptno from dept where 
LOC='CHICAGO')

59) Display the Job groups having total salary greater than the maximum 
salary for managers.
SQL>SELECT JOB,SUM(SAL) FROM EMP GROUP BY JOB HAVING SUM(SAL)>(SELECT 
MAX(SAL) FROM EMP WHERE JOB='MANAGER');

60) Display the names of employees from department number 10 with salary 
grether than that of any employee working in other department.
SQL>select ename from emp where deptno=10 and sal>any(select sal from 
emp where deptno not in 10).

61) Display the names of the employees from department number 10 with 
salary greater than that of all employee working in other departments.
SQL>select ename from emp where deptno=10 and sal>all(select sal from 
emp where deptno not in 10).

62) Display the names of the employees in Uppercase.
SQL>select upper(ename)from emp

63) Display the names of the employees in Lowecase.
SQL>select lower(ename)from emp

64) Display the names of the employees in Propercase.
SQL>select initcap(ename)from emp;

65) Display the length of Your name using appropriate function.
SQL>select length('name') from dual

66) Display the length of all the employee names.
SQL>select length(ename) from emp;

67) select name of the employee concatenate with employee number. 
SQL>select ename||empno from emp;

68) User appropriate function and extract 3 characters starting from 2 
characters from the following  string 'Oracle'. i.e the out put should be 'ac'.
SQL>select substr('oracle',3,2) from dual

69) Find the First occurance of character 'a' from the following string i.e 
'Computer Maintenance Corporation'.
SQL>SELECT INSTR('Computer Maintenance Corporation','a',1) FROM DUAL

70) Replace every occurance of alphabhet A with B in the string Allens(use 
translate function)
SQL>select translate('Allens','A','B') from dual

71) Display the informaction from emp table.Where job manager is found it 
should be displayed as boos(Use replace function).
SQL>select replace(JOB,'MANAGER','BOSS') FROM EMP;

72) Display empno,ename,deptno from emp table.Instead of display department 
numbers display the related department name(Use decode function).
SQL>select empno,ename,decode(deptno,10,'ACCOUNTING',20,'RESEARCH',30,'SALES',40,'OPRATIONS') from emp;

73) Display your age in days.
SQL>select to_date(sysdate)-to_date('10-sep-77')from dual

74) Display your age in months.
SQL>select months_between(sysdate,'10-sep-77') from dual

75) Display the current date as 15th Augest Friday Nineteen Ninety Saven.
SQL>select to_char(sysdate,'ddth Month day year') from dual

76) Display the following output for each row from emp table.

scott has joined the company on wednesday 13th August ninten nintey.
SQL>select ENAME||' HAS JOINED THE COMPANY ON  '||to_char(HIREDATE,'day 
ddth Month  year')   from EMP;

77) Find the date for nearest saturday after current date.
SQL>SELECT NEXT_DAY(SYSDATE,'SATURDAY')FROM DUAL;

78) Display current time.
SQL>select to_char(sysdate,'hh:MM:ss') from dual.

79) Display the date three months Before the current date.
SQL>select add_months(sysdate,3) from dual;

80) Display the common jobs from department number 10 and 20.
SQL>select job from emp where deptno=10 and job in(select job from emp 
where deptno=20);

81) Display the jobs found in department 10 and 20 Eliminate duplicate jobs.
SQL>select distinct(job) from emp where deptno=10 or deptno=20
           (or)
SQL>select distinct(job) from emp where deptno in(10,20);

82) Display the jobs which are unique to department 10.
SQL>select distinct(job) from emp where deptno=10

83) Display the details of those who do not have any person working under them.
SQL>select e.ename from emp,emp e where emp.mgr=e.empno group by 
e.ename having count(*)=1;

84) Display the details of those employees who are in sales department and 
grade is 3.

SQL>select * from emp where deptno=(select deptno from dept where 
dname='SALES')and sal between(select losal from salgrade where grade=3)and
	(select hisal from salgrade where grade=3);

85) Display those who are not managers and who are managers any one.
i)display the managers names
SQL>select distinct(m.ename) from emp e,emp m where m.empno=e.mgr;

ii)display the who are not managers 
SQL>select ename from emp where ename not in(select distinct(m.ename) 
         from emp e,emp m where m.empno=e.mgr);

86) Display those employee whose name contains not less than 4 characters.
SQL>select ename from emp where length(ename)>4;

87) Display those department whose name start with "S" while the location 
name ends with "K".
SQL>select dname from dept where dname like 'S%' and loc like '%K';

88) Display those employees whose manager name is JONES.
SQL>select p.ename from emp e,emp p where e.empno=p.mgr and 
e.ename='JONES';

89) Display those employees whose salary is more than 3000 after giving 20% 
increment.
SQL>select ename,sal from emp where (sal+sal*.2)>3000;

90) Display all employees while their dept names;
SQL>select ename,dname from emp,dept where emp.deptno=dept.deptno

91) Display ename who are working in sales dept.
SQL>select ename from emp where deptno=(select deptno from dept where 
dname='SALES');

92) Display employee name,deptname,salary and comm for those sal in between 
2000 to 5000 while location is chicago.
SQL>select ename,dname,sal,comm from emp,dept where sal  between 2000 
and 5000 
          and loc='CHICAGO' and emp.deptno=dept.deptno;

93)Display those employees whose salary greter than his manager salary.
SQL>select p.ename from emp e,emp p where e.empno=p.mgr and p.sal>e.sal

94) Display those employees who are working in the same dept where his 
manager is work.
SQL>select p.ename from emp e,emp p where e.empno=p.mgr and 
p.deptno=e.deptno;

95) Display those employees who are not working under any manager.
SQL>select ename from emp where mgr is null

96) Display grade and employees name for the dept no 10 or 30 but grade is 
not 4 while joined the company before 31-dec-82.
SQL>select ename,grade from emp,salgrade where sal between losal and 
hisal and deptno     in(10,30) and grade<>4 and hiredate<'31-DEC-82';

97) Update the salary of each employee by 10% increment who are not 
eligiblw for commission.
SQL>update emp set sal=sal+sal*10/100 where comm is null;

98) SELECT those employee who joined the company before 31-dec-82 while 
their dept location is newyork or  Chicago.
SQL>SELECT EMPNO,ENAME,HIREDATE,DNAME,LOC FROM EMP,DEPT
 WHERE (EMP.DEPTNO=DEPT.DEPTNO)AND 
HIREDATE <'31-DEC-82' AND DEPT.LOC IN('CHICAGO','NEW YORK');
 
99) DISPLAY EMPLOYEE NAME,JOB,DEPARTMENT,LOCATION FOR ALL WHO ARE WORKING 
AS  MANAGER?
SQL>select ename,JOB,DNAME,LOCATION from emp,DEPT where mgr is not 
null;

100) DISPLAY THOSE EMPLOYEES WHOSE MANAGER NAME IS JONES? --
          [AND ALSO DISPLAY THEIR MANAGER NAME]?
SQL> SELECT P.ENAME FROM EMP E, EMP P WHERE E.EMPNO=P.MGR AND 
E.ENAME='JONES';

101) Display name and salary of ford if his salary is equal to hisal of his 
grade
a)select ename,sal,grade from emp,salgrade where sal between losal and 
hisal
 and ename ='FORD' AND HISAL=SAL;

102) Display employee name,job,depart name ,manager name,his grade and make 
out an under department wise?
SQL>SELECT E.ENAME,E.JOB,DNAME,EMP.ENAME,GRADE FROM EMP,EMP 
E,SALGRADE,DEPT
WHERE EMP.SAL BETWEEN LOSAL AND HISAL AND EMP.EMPNO=E.MGR
 AND EMP.DEPTNO=DEPT.DEPTNO ORDER BY DNAME

103) List out all employees name,job,salary,grade and depart name for every 
one in the company  except 'CLERK'.Sort on salary display the highest salary?
SQL>SELECT ENAME,JOB,DNAME,SAL,GRADE FROM EMP,SALGRADE,DEPT WHERE 
SAL BETWEEN LOSAL AND HISAL AND EMP.DEPTNO=DEPT.DEPTNO AND JOB
 NOT IN('CLERK')ORDER BY SAL ASC;

104) Display the employee name,job and his manager.Display also employee who 
are without manager?
SQL>select e.ename,e.job,eMP.ename AS Manager from emp,emp e where 
emp.empno(+)=e.mgr

105) Find out the top 5 earners of company?
SQL>SELECT DISTINCT SAL FROM EMP E WHERE 5>=(SELECT COUNT(DISTINCT SAL) 
FROM 
           EMP A WHERE A.SAL>=E.SAL)ORDER BY SAL DESC;


106) Display name of those employee who are getting the highest salary?
SQL>select ename from emp where sal=(select max(sal) from emp);

107) Display those employee whose salary is equal to average of maximum and 
minimum?
SQL>select ename from emp where sal=(select max(sal)+min(sal)/2 from 
emp);

108) Select count of employee in each department  where count greater than 3?
SQL>select count(*) from emp group by deptno having count(deptno)>3

109) Display dname where at least 3 are working and display only department 
name?
SQL>select distinct d.dname from dept d,emp e where d.deptno=e.deptno 
and 3>any
           (select count(deptno) from emp group by deptno)

110) Display name of those managers name whose salary is more than average 
salary of his company?
SQL>SELECT E.ENAME,EMP.ENAME FROM EMP,EMP E 
           WHERE EMP.EMPNO=E.MGR AND E.SAL>(SELECT AVG(SAL) FROM EMP);

111)Display those managers name whose salary is more than average salary of 
his employee?
SQL>SELECT DISTINCT EMP.ENAME FROM EMP,EMP E WHERE
            E.SAL <(SELECT AVG(EMP.SAL) FROM EMP 
            WHERE EMP.EMPNO=E.MGR GROUP BY EMP.ENAME) AND 
EMP.EMPNO=E.MGR;

112) Display employee name,sal,comm and net pay for those employee 
whose net pay is greter than or equal to any other employee salary of 
the company?
SQL>select ename,sal,comm,sal+nvl(comm,0) as NetPay from emp 
          where sal+nvl(comm,0) >any (select sal from emp)


113) Display all employees names with total sal of company with each 
employee name?
SQL>SELECT ENAME,(SELECT SUM(SAL)  FROM EMP) FROM EMP;

114) Find out last 5(least)earners of the company.?
SQL>SELECT DISTINCT SAL FROM EMP E WHERE
           5>=(SELECT COUNT(DISTINCT SAL) FROM EMP A WHERE 
A.SAL<=E.SAL)
           ORDER BY SAL DESC;

115) Find out the number of employees whose salary is greater than their 
manager salary?
SQL>SELECT E.ENAME FROM EMP ,EMP E WHERE EMP.EMPNO=E.MGR 
        AND EMP.SAL<E.SAL;

116) Display those department where no employee working?
SQL>select dname from emp,dept where emp.deptno not in(emp.deptno)

117) Display those employee whose salary is ODD value?
SQL>select * from emp where sal<0;

118) Display those employee whose salary contains alleast 3 digits?
SQL>select * from emp where length(sal)>=3;

119) Display those employee who joined in the company in the month of Dec?
SQL>select ename from emp where to_char(hiredate,'MON')='DEC';

120) Display those employees whose name contains "A"?
SQL>select ename from emp where instr(ename,'A')>0;
		or
SQL>select ename from emp where ename like('%A%');

121) Display those employee whose deptno is available in salary?
SQL>select emp.ename from emp, emp e where emp.sal=e.deptno;

122) Display those employee whose first 2 characters from hiredate -last 2 
characters of salary?
SQL>select ename,SUBSTR(hiredate,1,2)||ENAME||substr(sal,-2,2) from emp

123) Display those employee whose 10% of salary is equal to the year of 
joining?
SQL>select ename from emp where to_char(hiredate,'YY')=sal*0.1;

124) Display those employee who are working in sales or research?
SQL>SELECT ENAME FROM EMP WHERE DEPTNO IN(SELECT DEPTNO FROM DEPT WHERE 
           DNAME IN('SALES','RESEARCH'));

125) Display the grade of jones?
SQL>SELECT ENAME,GRADE FROM EMP,SALGRADE
            WHERE SAL BETWEEN LOSAL AND HISAL AND Ename='JONES';

126) Display those employees who joined the company before 15 of the month?
a)select ename from emp where to_char(hiredate,'DD')<15;

127) Display those employee who has joined before 15th of the month.
a)select ename from emp where to_char(hiredate,'DD')<15;

128) Delete those records where no of employees in a particular department 
is less than 3.
SQL>delete from emp where deptno=(select deptno from emp
           group by deptno having count(deptno)<3);


129) Display the name of the department where no employee working.
SQL> SELECT E.ENAME,E.JOB,M.ENAME,M.JOB FROM EMP E,EMP M
 WHERE E.MGR=M.EMPNO

130) Display those employees who are working as manager.
SQL>SELECT M.ENAME MANAGER FROM EMP M ,EMP E
WHERE E.MGR=M.EMPNO GROUP BY M.ENAME

131) Display those employees whose grade is equal to any number of sal but 
not equal to first number of sal?
SQL> SELECT ENAME,GRADE FROM EMP,SALGRADE
            WHERE GRADE NOT IN(SELECT SUBSTR(SAL,0,1)FROM EMP)

132) Print the details of all the employees who are Sub-ordinate to BLAKE?
SQL>select emp.ename from emp, emp e where emp.mgr=e.empno and 
e.ename='BLAKE';


133) Display employee name and his salary whose salary is greater than 
  highest average of department number?
SQL>SELECT SAL FROM EMP WHERE SAL>(SELECT MAX(AVG(SAL)) FROM EMP
         GROUP BY DEPTNO);

134) Display the 10th record of emp table(without using rowid)
SQL>SELECT * FROM EMP WHERE ROWNUM<11
	MINUS
	SELECT * FROM EMP WHERE ROWNUM<10 

135) Display the half of the enames in upper case and remaining lowercase?
SQL>

SELECT 
SUBSTR(LOWER(ENAME),1,3)||SUBSTR(UPPER(ENAME),3,LENGTH(ENAME)) 
           FROM EMP;

136) Display the 10th record of emp table without using group by and rowid?
SQL>SELECT * FROM EMP WHERE ROWNUM<11
	MINUS
	SELECT * FROM EMP WHERE ROWNUM<10 

	Delete the 10th record of emp table.
SQL>DELETE FROM EMP WHERE EMPNO=(SELECT EMPNO FROM EMP WHERE ROWNUM<11
	MINUS
	SELECT EMPNO FROM EMP WHERE ROWNUM<10)

137) Create a copy of emp table;
SQL>create table new_table as select * from emp where 1=2;
  
138) Select ename if ename exists more than once.
SQL>select ename  from emp e group by ename having count(*)>1;

139) Display all enames in reverse order?(SMITH:HTIMS).
SQL>SELECT REVERSE(ENAME)FROM EMP;

140) Display those employee whose joining of month and grade is equal.
SQL>SELECT ENAME FROM EMP WHERE SAL BETWEEN
           (SELECT LOSAL FROM SALGRADE WHERE 
             GRADE=TO_CHAR(HIREDATE,'MM')) AND
        (SELECT HISAL FROM SALGRADE WHERE 
GRADE=TO_CHAR(HIREDATE,'MM'));
	
141) Display those employee whose joining DATE is available in deptno.
SQL>SELECT ENAME FROM EMP WHERE TO_CHAR(HIREDATE,'DD')=DEPTNO

142) Display those employees name as follows
               A ALLEN
               B BLAKE
SQL> SELECT SUBSTR(ENAME,1,1),ENAME FROM EMP;

143) List out the employees ename,sal,PF(20% OF SAL) from emp;
SQL>SELECT ENAME,SAL,SAL*.2 AS PF FROM EMP;	


144) Create table emp with only one column empno;
SQL>Create table emp as select empno from emp where 1=2;

145) Add this column to emp table ename vrachar2(20).
SQL>alter table emp add(ename varchar2(20));

146) Oops I forgot give the primary key constraint.  Add in now.
SQL>alter table emp add primary key(empno);

147) Now increase the length of ename column to 30 characters.
SQL>alter table emp modify(ename varchar2(30));

148) Add salary column to emp table.
SQL>alter table emp add(sal number(10));

149) I want to give a validation saying that salary cannot be greater 10,000
(note give a name to this constraint)
SQL>alter table emp add constraint chk_001 check(sal<=10000)

150) For the time being I have decided that I will not impose this validation.My boss has agreed to pay more than 10,000.
SQL>again alter the table or drop constraint with  alter table emp drop constraint chk_001 (or)Disable the constraint by using  alter table emp modify constraint chk_001 disable;

151) My boss has changed his mind.  Now he doesnt want to pay more than 
10,000.so revoke that salary constraint.
SQL>alter table emp modify constraint chk_001 enable;

152) Add column called as mgr to your emp table;
SQL>alter table emp add(mgr number(5));

153) Oh! This column should be related to empno.  Give a command to add this 
constraint.
SQL>ALTER TABLE EMP ADD CONSTRAINT MGR_DEPT FOREIGN KEY(MGR) REFERENCES 
EMP(EMPNO)
                   		
154) Add deptno column to your emp table;
SQL>alter table emp add(deptno number(5));	

155) This deptno column should be related to deptno column of dept table;
SQL>alter table emp add constraint dept_001 foreign key(deptno) 
reference dept(deptno)  
	[deptno should be primary key]

156) Give the command to add the constraint.
SQL>alter table <table_name) add constraint <constraint_name> 
<constraint type>

157) Create table called as newemp.  Using single command create this table 
as well as get data into this table(use create table as);
SQL>create table newemp as select * from emp;

SQL>Create table called as newemp.  This table should contain only 
empno,ename,dname.
SQL>create table newemp as select empno,ename,dname from emp,dept where 
1=2;

158) Delete the rows of employees who are working in the company for more 
than 2 years.
SQL>delete from emp where (sysdate-hiredate)/365>2;

159) Provide a commission(10% Comm Of Sal) to employees who are not earning 
any commission.
SQL>select sal*0.1 from emp where comm is null

160) If any employee has commission his commission should be incremented by 
10% of his salary.
SQL>update emp set comm=sal*.1 where comm is not null;

161) Display employee name and department name for each employee.
SQL>select empno,dname from emp,dept where emp.deptno=dept.deptno

162)Display employee number,name and location of the department in which he 
is working.
SQL>select empno,ename,loc,dname from emp,dept where 
emp.deptno=dept.deptno;

163) Display ename,dname even if there are no employees working in a 
particular department(use outer join).
SQL>select ename,dname from emp,dept where emp.deptno=dept.deptno(+)

164) Display employee name and his manager name.
SQL>select p.ename,e.ename from emp e,emp p where e.empno=p.mgr;

165) Display the department name and total number of employees in each 
department.
SQL>select dname,count(ename) from emp,dept where 
emp.deptno=dept.deptno group by dname;

166)Display the department name along with total salary in each department.
SQL>select dname,sum(sal) from emp,dept where emp.deptno=dept.deptno 
group by dname;

167) Display itemname and total sales amount for each item.
SQL>select itemname,sum(amount) from item group by itemname;

168) Write a Query To Delete The Repeted Rows from emp table;
SQL>Delete from emp where rowid not in(select min(rowid)from emp group 
by ename)
	
169) TO DISPLAY 5 TO 7 ROWS FROM A TABLE
SQL>select ename from emp
         where rowid in(select rowid from emp where rownum<=7
         minus
  select rowid from empi where rownum<5)

170)  DISPLAY  TOP N ROWS FROM TABLE?

SQL>SELECT * FROM 
	(SELECT *  FROM EMP ORDER BY ENAME DESC)
	 WHERE ROWNUM <10;

171) DISPLAY   TOP 3 SALARIES FROM EMP;
SQL>SELECT SAL FROM ( SELECT  * FROM EMP ORDER  BY SAL DESC )
                   WHERE ROWNUM <4

172) DISPLAY  9th FROM THE EMP TABLE?
SQL>SELECT ENAME FROM EMP
 	WHERE ROWID=(SELECT ROWID FROM EMP WHERE ROWNUM<=10
 	MINUS
 	SELECT ROWID FROM EMP WHERE ROWNUM <10)
	select second max salary from emp;
	select max(sal) fromemp where sal<(select  max(sal) from emp);


------******------
