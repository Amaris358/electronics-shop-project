from src.keyboard import Keyboard
import pytest

kb_one = Keyboard("HyperX Alloy", 6000, 79)


def test_keyboard():
    assert kb_one.language == "EN"
    kb_one.change_lang()
    assert kb_one.language == "RU"
    kb_one.change_lang()
    assert kb_one.language == "EN"

    with pytest.raises(AttributeError):
        kb_one.language = "CH"
