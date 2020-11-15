--Подсчитайте средний возраст пользователей в таблице users.

select AVG(timestampdiff(YEAR, birthday_at, NOW())) from users;