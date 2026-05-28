# Write your MySQL query statement below

WITH cte AS (
    SELECT stock_name,operation, SUM(price) AS cost FROM Stocks 
    GROUP BY stock_name, operation
    ORDER BY stock_name, operation
),
cte2 as (
    SELECT stock_name, 
    cost - LEAD(cost,1) OVER(PARTITION BY stock_name ORDER BY stock_name, operation) AS capital_gain_loss FROM CTE 
)
SELECT stock_name , capital_gain_loss FROM cte2 
where capital_gain_loss is not null
