SELECT 
	t.date
    ,t.total
    ,t.userId
    ,n.name
FROM transactions as t
JOIN username AS u 
ON t.userId = u.A
JOIN name AS n 
ON u.B = n.id;