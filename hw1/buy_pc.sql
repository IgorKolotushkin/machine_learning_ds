select maker from product
where type = 'PC' and maker not in (
select maker from product
             where type = 'Laptop'
             )