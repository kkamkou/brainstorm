-- https://oj.leetcode.com/problems/nth-highest-salary/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE mx INT;
  DECLARE v1 INT DEFAULT N;

  SET mx = (SELECT MAX(`Salary`) FROM `Employee`);

  loop1: LOOP
    SET v1 = v1 - 1;

    IF v1 > 0 THEN
      SET mx = (SELECT MAX(`Salary`) FROM `Employee` WHERE `Salary` < mx);
      ITERATE loop1;
    END IF;

    LEAVE loop1;
  END LOOP loop1;

RETURN mx;
END
