from cut import range2tuple, list2slice

class TestRange2Tuple:

    def test_single_integer(self):
        assert range2tuple('1') == (0, 1)

    def test_upto_n(self):
        assert range2tuple('-5') == (None, 5)

    def test_from_n(self):
        assert range2tuple('5-') == (4, None)

    def test_n_to_m(self):
        assert range2tuple('3-5') == (2, 5)


class TestList2Slice:

    def test_single_range(self):
        assert list2slice('3-5') == [slice(2, 5)]

    def test_two_ranges(self):
        assert list2slice('-1,3-5') == [slice(None, 1), slice(2, 5)]