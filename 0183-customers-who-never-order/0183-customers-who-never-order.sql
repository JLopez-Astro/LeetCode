# Write your MySQL query statement below
select customers.name as Customers
from Customers
left join Orders
on Customers.id = Orders.Customerid
where Orders.Customerid is NULL