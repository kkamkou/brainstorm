-- https://oj.leetcode.com/problems/customers-who-never-order/

SELECT c.`Name` FROM `Customers` c
  LEFT JOIN `Orders` o ON(o.`CustomerId` = c.`Id`)
    WHERE o.`Id` IS NULL
