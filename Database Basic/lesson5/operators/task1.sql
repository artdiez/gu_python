--- Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.

ALTER TABLE snet2910.users ADD updated_at DATETIME NULL;
UPDATE users SET created_at = now(), updated_at = now();