# Write your MySQL query statement below
SELECT UNIQUE_ID, NAME FROM EMPLOYEES 
left join EMPLOYEEUNI on 
EMPLOYEES.id=EMPLOYEEUNI.id;