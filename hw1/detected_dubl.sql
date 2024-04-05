SELECT * FROM (
    SELECT
        code,
        ROW_NUMBER() OVER (PARTITION BY model, speed, ram, hd, cd, price ORDER BY code)
FROM pc) dbl