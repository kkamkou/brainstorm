-- https://oj.leetcode.com/problems/second-highest-salary/

-- best variant
SELECT MAX(`Salary`) FROM `Employee`
  WHERE `Salary` < (SELECT MAX(`Salary`) FROM `Employee`);

-- flexible variant
SELECT *
  FROM (
    SELECT `Salary` FROM `Employee`
      WHERE `Salary` != (SELECT MAX(`Salary`) FROM `Employee`)
  UNION
    SELECT NULL
  ) AS `SecondHighestSalary` ORDER BY `Salary` DESC LIMIT 1
