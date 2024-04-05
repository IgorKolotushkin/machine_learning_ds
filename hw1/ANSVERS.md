## Задания и ответы

1. создать все указанные таблицы - реализовано в main.py;
2. наполнить их данными (как минимум по 100 значений) - реализовано в main.py;
3. Напишите запросы к базе данных.
4. Найдите модели принтеров, имеющих самую высокую цену. Вывести: model, price:
```sql
SELECT model, price FROM printer
WHERE price = (SELECT max(price) FROM printer)
```

5. Найдите среднюю скорость ПК:
```sql
SELECT round(avg(speed), 2) FROM pc
```
6. Найдите производителя, продающего ПК, но не ноутбуки:
```sql
SELECT maker FROM product
WHERE type = 'PC' AND maker NOT IN (
SELECT maker FROM product
             WHERE type = 'Laptop'
             )
GROUP BY maker
```
7. Загрязните специально датасет (вставьте новые значения с уникальным кодом, но всеми остальными дублирующими полями).
Реализовано в main.py функция add_duplicate.

8. Напишите оконную функцию, которая поможет вам обнаружить эти строки-редиски.
```sql
SELECT * FROM (
    SELECT
        code,
        ROW_NUMBER() OVER (PARTITION BY model, speed, ram, hd, cd, price ORDER BY code)
FROM pc) dbl
```
9. Обновите название колонки в таблице printer с color на color_type и поменяйте тип поля:
```sql
ALTER TABLE printer
RENAME COLUMN color TO color_type;
```
10. В последнем пункте выполните слияние двух запросов из таблиц PC и Laptop, 
выбрав только те значения, у которых цена больше 500, а ram = 64:
```sql
SELECT code, model, price, ram, hd FROM pc
WHERE ram = 64 AND price > 500
UNION 
SELECT code, model, price, ram, hd FROM laptop
WHERE ram = 64 AND price > 500
```