from approximations import set_cover
import pytest


def test_set_cover_exceptions():
    with pytest.raises(ValueError):
        set_cover({1}, [], [2])

    with pytest.raises(ValueError):
        set_cover({1}, [{1}], [2])

    with pytest.raises(ValueError):
        set_cover({1}, [{1}, {1}], [2])


def test_set_cover():
    cover = set_cover(
        {1, 2, 3, 4, 5},
        [{1, 2}, {3}, {1, 2, 3, 4}, {1, 3, 5}],
        [1, 2, 3, 4]
    )
    assert cover == [0, 2, 3]
