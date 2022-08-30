# Write your MySQL query statement below
select A.name as Customers
from Customers A
where not exists
(select B.customerId from orders B where B.customerId = A.Id)