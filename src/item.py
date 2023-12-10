import csv
import typing


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise Exception

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name: typing.Any) -> None:
        """
        Создает экземпляры класса из файла csv.
        """
        with open(file_name, "r") as file:
            dict_reader = csv.DictReader(file, delimiter=",")
            for row in dict_reader:
                name = row["name"]
                price = Item.string_to_number(row["price"])
                quantity = Item.string_to_number(row["quantity"])
                Item.all.append(cls(name, price, quantity))

                

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[:10]

    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Преобразование строки в число.
        """
        if string.isdigit():
            return int(string)
        return int(float(string))



