-- https://oj.leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT e1.`Name`
  FROM `Employee` e1
  INNER JOIN `Employee` e2 ON(e2.`Id` = e1.`ManagerId`)
    WHERE e1.`Salary` > e2.`Salary`
