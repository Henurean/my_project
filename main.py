



def a(price, per):
    b = price - (price * per / 100)
    return b
ish = float(input("Введите исходную цену товара: "))
ski = float(input("Введите процент скидки (например, 15): "))
fin = a(ish, ski)
print("Исходная цена:", ish)
print("Процент скидки:", ski)
print("Итоговая цена:", fin)