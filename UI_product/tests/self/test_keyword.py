
from libs import action


def test_key_get():
    key_word = action.KeyWord  # 类方法可以不用实例化

    assert "get" in key_word.all_keyword()
