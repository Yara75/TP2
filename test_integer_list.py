import pytest
from integer_list import IntegerList


class TestIntegerList:

    @pytest.mark.parametrize("maList, elem, res", [([4, 6, 9, 10], 1, [4, 6, 9, 10, 1]),
                                                   ([4.0, 4.5, 10.12], 9.99, [4.0, 4.5, 10.12, 9.99]),
                                                   ([], 10, [10]),
                                                   ([], 9.0001, [9.0001]),
                                                   (["234", 9.0, True], {"test"}, ["234", 9.0, True, {"test"}])])
    def test_add_integer(self, maList, elem, res):
        integL = IntegerList(maList)
        integL.add_integer(elem)
        assert integL.list == res
