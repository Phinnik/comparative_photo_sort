import pytest

from src.sorting import Sorter


class TestSorter:
    def test_sort_empty_array(self):
        sorter = Sorter([])
        sorter.sort()
        assert sorter.array == []

    def test_sort_sorted_array(self):
        input_array = [1, 2, 3, 4, 5]
        expected_array = [1, 2, 3, 4, 5]
        sorter = Sorter(input_array)
        sorter.sort()
        assert sorter.array == expected_array

    def test_sort_reverse_sorted_array(self):
        input_array = [5, 4, 3, 2, 1]
        expected_array = [1, 2, 3, 4, 5]
        sorter = Sorter(input_array)
        sorter.sort()
        assert sorter.array == expected_array

    def test_sort_random_array(self):
        input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_array = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        sorter = Sorter(input_array)
        sorter.sort()
        assert sorter.array == expected_array

    def test_sort_with_custom_comparison(self):
        def custom_comparison(left, right):
            return left < right

        input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        expected_array = [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
        sorter = Sorter(input_array)
        sorter._is_greater = custom_comparison  # pylint: disable=W0212
        sorter.sort()
        assert sorter.array == expected_array


# Run the tests
if __name__ == "__main__":
    pytest.main()
