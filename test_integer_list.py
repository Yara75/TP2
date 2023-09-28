import pytest
from integer_list import IntegerList


class TestIntegerList:

    @pytest.mark.parametrize("maList, elem, res", [([4, 6, 9, 10], 1, [4, 6, 9, 10, 1]),
                                                   ([4.0, 4.5, 10.12], 9.99, [4.0, 4.5, 10.12, 9.99]),
                                                   ([], 10, [10]),
                                                   ([], 9.0001, [9.0001]),
                                                   (["234", 9.0, True], {"test"}, ["234", 9.0, True, {"test"}])])
    def test_add_element(self, maList, elem, res):
        listElems = IntegerList(maList)
        listElems.add_integer(elem)
        assert listElems.list == res

    @pytest.mark.parametrize("res, elem, maList", [([4, 6, 9, 10], 1, [4, 6, 9, 10, 1]),
                                                   ([4.0, 4.5, 10.12], 9.99, [4.0, 4.5, 10.12, 9.99]),
                                                   ([], 10, [10]),
                                                   ([], 9.0001, [9.0001]),
                                                   (["234", 9.0, True], {"test"}, ["234", 9.0, True, {"test"}])])
    def test_remove_element(self, res, elem, maList):
        listElems = IntegerList(maList)
        listElems.remove_integer(elem)
        assert listElems.list == res

    @pytest.mark.parametrize("res, elemA, elemB, maList", [([4, 6, 10], 9, 1, [4, 6, 9, 10, 1]),
                                                           ([4.0, 4.5], 10.12, 9.99, [4.0, 4.5, 10.12, 9.99]),
                                                           ([], 10, 5, [5, 10]),
                                                           ([], 7.1, 9.0001, [9.0001, 7.1])])
    def test_remove_elements(self, res, elemA, elemB, maList):
        listElems = IntegerList(maList)
        listElems.remove_integer(elemA)
        listElems.remove_integer(elemB)
        assert listElems.list == res

    @pytest.mark.parametrize("maList, elem", [([3, 5, 6], 2),
                                              ([15143, 2432432, 2342], 5.5),
                                              ([12.34, 1341.2352, 14234.24], 6)])
    def test_remove_elem_not_in_the_list(self, maList, elem):
        listElems = IntegerList(maList)
        with pytest.raises(Exception):
            listElems.remove_integer(elem)
