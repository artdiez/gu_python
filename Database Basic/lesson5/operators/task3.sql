--В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0,
--если товар закончился и выше нуля, если на складе имеются запасы.
--Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value.
--Однако нулевые запасы должны выводиться в конце, после всех записей.

INSERT INTO storehouses_products (storehouse_id, product_id, value) VALUES (1, 1, 0), (2, 2, 0), (1, 5, 5), (5, 6, 6);

SELECT * FROM storehouses_products ORDER BY CASE WHEN value = 0 THEN 1 ELSE 0 END, value;
