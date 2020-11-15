--Таблица users была неудачно спроектирована.
--Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10.
--Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.

ALTER TABLE users ADD new_created_at DATETIME, new_updated_at DATETIME;
UPDATE users
SET new_created_at = STR_TO_DATE(created_at, '%d.%m.%Y %h:%i'),
    new_updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');
ALTER TABLE users 
    DROP created_at, DROP updated_at, 
    RENAME COLUMN new_created_at TO created_at, RENAME COLUMN new_updated_at TO updated_at;