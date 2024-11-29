class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл с продуктами не найден."

    def add(self, *products):
        existing_products = set()
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    name, weight, category = line.strip().split(', ')
                    existing_products.add((name, weight, category))
        except FileNotFoundError:
            pass

        with open(self.__file_name, 'a') as file:
            for product in products:
                product_tuple = (product.name, str(product.weight), product.category)
                if product_tuple not in existing_products:
                    file.write(f"{product}\n")
                    existing_products.add(product_tuple)
                else:
                    print(f"Продукт {product.name} уже есть в магазине")

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
