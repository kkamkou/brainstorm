-- https://oj.leetcode.com/problems/duplicate-emails/

SELECT p1.`Email`
  FROM `Person` p1, `Person` p2
    WHERE p1.`Id` != p2.`Id` AND p1.`Email` = p2.`Email`
