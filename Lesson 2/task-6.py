n = int(input("Сколько видов товаров? "))
i = 1
product_list = []
analytics = []
while i <= n:
    name = input(f"Введите название {i} товара: ")
    cost = input(f"Введите стоимость {i} товара: ")
    quantity = input(f"Введите колличетсво {i} товара: ")
    product = (i, {'Название': name, 'цена': cost, 'колличество': quantity})
    product_list.append(product)
    i +=1
for el in product_list:
    print(el)