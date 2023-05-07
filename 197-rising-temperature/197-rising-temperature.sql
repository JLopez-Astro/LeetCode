# Write your MySQL query statement below
select wA.id
from Weather as wA, Weather as wB
where wA.Temperature > wB.Temperature
and datediff(wA.recordDate, wB.recordDate) = 1