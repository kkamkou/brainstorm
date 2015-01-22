-- https://oj.leetcode.com/problems/department-highest-salary/

SELECT
    d.`Name` AS `Department`, e.`Name` AS `Employee`, e.`Salary` AS `Salary`
  FROM `Employee` e
  LEFT JOIN `Department` d ON(d.`Id` = e.`DepartmentId`)
  INNER JOIN (
    SELECT `DepartmentId`, MAX(`Salary`) AS `Salary`
      FROM `Employee`
        GROUP BY `DepartmentId`
  ) AS e2 USING(`DepartmentId`, `Salary`)
    WHERE d.`Id`;
