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

    @pytest.mark.parametrize("maList, res", [([4, 6, 9, 10], 7.25),  # Liste d'entiers
                                             ([4.5, 4.5, 10.5], 6.5),  # Liste de flottants
                                             ([], 0),  # Liste vide
                                             (["234", 9.0, True], 5.0),  # Liste mixte
                                             ([True, False], 0.5),  # Liste de booléens
                                             (["abc", "def"], 0),  # Liste de chaînes
                                             ([None, None], 0),  # Liste de valeurs None
                                             ([10], 10),  # Liste avec un seul élément
                                             ([-1, -2, -3], -2)  # Liste de nombres négatifs
                                             ])
    def test_get_average(self, maList, res):
        listElems = IntegerList(maList)
        assert listElems.get_average() == res

    @pytest.mark.parametrize("maList, elem", [([8, 14, 1], 14),
                                              ([956, 123, 1966], 1966),
                                              ([14.75, 8549.27, 0.1], 8549.27)])
    def test_get_max(self, maList, elem):
        listElems = IntegerList(maList)
        assert listElems.get_max() == elem

    @pytest.mark.parametrize("maList, elem", [([8, 14, 1], 1),
                                              ([956, 123, 1966], 123),
                                              ([14.75, 8549.27, 0.1], 0.1)])
    def test_get_min(self, maList, elem):
        listElems = IntegerList(maList)
        assert listElems.get_min() == elem

    @pytest.mark.parametrize("maList, elem", [([8, 14, 1], 23),
                                              ([956, 123, 1966], 3045),
                                              ([14.75, 8549.27, 0.1], 8564,12)])
    def test_get_sum(self, maList, elem):
        listElems = IntegerList(maList)
        assert listElems.get_sum() == elem

    @pytest.mark.parametrize("maList, elem", [([8, 14, 1], 28,22),
                                              ([96, 23, 196], 5028,67),
                                              ([14.7, 84.27, 0.1], 1348,64)])
    def test_get_variance(self, maList, elem):
        listElems = IntegerList(maList)
        assert listElems.get_variance() == elem

    @pytest.mark.parametrize("maList, elem", [([8, 14, 1], 5,31),
                                              ([96, 23, 196], 70,91),
                                              ([14.7, 84.27, 0.1], 36.72)])
    def test_get_ecartype(self, maList, elem):
        listElems = IntegerList(maList)
        assert listElems.get_ecartype() == elem


