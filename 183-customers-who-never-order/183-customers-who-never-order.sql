# Write your MySQL query statement below
select Customers.name as Customers
from Customers
where not exists
(select Orders.customerId from Orders where Orders.customerId = Customers.Id)