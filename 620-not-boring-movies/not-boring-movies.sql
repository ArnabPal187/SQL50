# Write your MySQL query statement below
SELECT
*
FROM CINEMA C
WHERE C.DESCRIPTION<>'boring' AND C.ID%2<>0
ORDER BY C.RATING DESC;