select code, model, price, ram, hd from pc
where ram = 64 and price > 500
union
select code, model, price, ram, hd from laptop
where ram = 64 and price > 500