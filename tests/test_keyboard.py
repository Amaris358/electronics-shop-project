from src.keyboard import Keyboard
import pytest

kb = Keyboard("HyperX Alloy", 6000, 79)


def test_keyboard():
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

    with pytest.raises(AttributeError):
        kb.language = "CH"
