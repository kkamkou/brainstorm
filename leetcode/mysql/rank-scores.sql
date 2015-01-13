-- https://oj.leetcode.com/problems/rank-scores/

SELECT
  s2.`Score`,
  (SELECT COUNT(DISTINCT s1.`Score`) FROM `Scores` s1 WHERE s1.`Score` >= s2.`Score`)
    FROM `Scores` s2
      ORDER BY s2.`Score` DESC
