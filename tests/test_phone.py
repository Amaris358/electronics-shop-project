import pytest

from src.phone import Phone

phone_1 = Phone("Samsung A9", 80000, 100, 2)


def test_phone():
    assert phone_1.name == "Samsung A9"
    assert phone_1.number_of_sim == 2


def test_repr():
    assert repr(phone_1) == "Phone('Samsung A9', 80000, 100, 2)"
    with pytest.raises(ValueError):
        phone_1.number_of_sim = -1
