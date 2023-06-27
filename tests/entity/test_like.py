from entity.like import Like

def test_like():
    assert Like(29).number_like == 29
    assert Like(29).number_like != 23
    assert Like(29).number_like >= 23
    assert Like(29).number_like <= 30
