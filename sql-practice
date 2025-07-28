-- ## Combine two tables -- leetcode
select p.firstName, p.lastName, a.city, a.state 
from Person p left join Address a 
on p.personId= a.personId;


-- ## SECOND HIGHEST SALARY -- leetcode
select Max(salary) as SecondHighestSalary
from Employee
where salary<(select Max(salary) from Employee)


-- ## EMPLOYEES EARNING MORE THAN THEIR MANAGERS -- leetcode
select e1.name as Employee 
from Employee e1 join Employee e2 
on e1.managerId = e2.id 
where e1.salary > e2.salary;


-- ## Customers who never placed an Order -- leetcode
select name as Customers 
from Customers where id not in 
  (select Customers.id 
  from Customers,Orders 
  where Customers.id = Orders.customerId);
