import pytest
import pandas as pd
from src.item import Item, InstantiateCSVError
from src.phone import Phone


item1 = Item('Микроволновая печь', 3000, 50)
item2 = Item('Телевизор', 50000, 10)
Item.pay_rate = 0.5


def test_item():
    assert item1.name == 'Микроволновая печь'
    assert item2.name == 'Телевизор'
    assert item1.price == 3000
    assert item2.price == 50000
    assert item1.quantity == 50
    assert item2.quantity == 10


def test_calculate_total_price():
    assert item1.calculate_total_price() == 150000
    assert item2.calculate_total_price() == 500000


def test_apply_discount():
    item2.apply_discount()
    assert item1.price == 3000
    assert item2.price == 25000


def test_string_to_number():
    assert Item.string_to_number('10.3') == 10
    assert Item.string_to_number('10.0') == 10

    assert Item.string_to_number('10') == 10


def test_name():
    item1.name = 'Микроволновая печь'
    item2.name = 'Пылесос'
    assert item1.name == 'Микроволно'
    assert item2.name == 'Пылесос'


def test_instantiate_from_csv():
    Item.instantiate_from_csv("../src/items.csv")
    assert len(Item.all) == 5
    item_one = Item.all[2]
    item_two = Item.all[3]
    assert item_one.name == "Кабель"
    assert item_one.price == 10
    assert item_two.name == "Мышка"
    assert item_two.quantity == 5


item_3 = Item('Зарядка', 500, 1000)
item_4 = Item('Холодильник', 30000, 100)


def test_str():
    assert str(item_3) == 'Зарядка'
    assert str(item_4) == 'Холодильник'


def test_repr():
    assert repr(item_3) == "Item('Зарядка', 500, 1000)"
    assert repr(item_4) == "Item('Холодильник', 30000, 100)"


item_test = Item('Утюг', 5000, 150)
phone_test = Phone("Xiaomi MI8", 16000, 20, 2)
phone_test2 = Phone("Oppo S7", 20000, 50, 2)


def test_add():
    assert item_test + phone_test == 170
    assert phone_test + phone_test2 == 70
    with pytest.raises(Exception):
        assert phone_test + item_test
        assert phone_test + 50


def test_exceptions():
    data_file = pd.read_csv("../src/items_broken.csv", encoding="utf-8")
    assert data_file.shape == (2, 2)
    with pytest.raises(FileNotFoundError):
        assert pd.read_csv("../src/no_file.csv")
    assert len(list(data_file.columns)) == 2
    with pytest.raises(InstantiateCSVError):
        assert Item.instantiate_from_csv("../src/items_broken.csv")

