from src.item import Item

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

