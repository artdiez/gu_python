--Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели.
--Следует учесть, что необходимы дни недели текущего года, а не года рождения.

SELECT
	COUNT(*) AS total,
	WEEKDAY(
		CONCAT(
			YEAR(NOW()),
			SUBSTR(birthday_at, 5)
		)
	) AS week_day
FROM
	users
GROUP BY
	week_day;