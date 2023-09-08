from typing import Optional


def _merge(array, left_idx: int, mid_idx: int, right_idx: int):
    left_array = array[left_idx : mid_idx + 1]
    right_array = array[mid_idx + 1 : right_idx + 1]

    i, j = 0, 0
    k = left_idx

    while (i < len(left_array)) and (j < len(right_array)):
        if left_array[i] > right_array[j]:
            array[k] = right_array[j]
            j += 1
        else:
            array[k] = left_array[i]
            i += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(
    array: list, left_idx: Optional[int] = None, right_idx: Optional[int] = None
):
    left_idx = left_idx if left_idx is not None else 0
    right_idx = right_idx if right_idx is not None else len(array) - 1

    if left_idx < right_idx:
        mid_idx = left_idx + (right_idx - left_idx) // 2

        merge_sort(array, left_idx, mid_idx)
        merge_sort(array, mid_idx + 1, right_idx)
        _merge(array, left_idx, mid_idx, right_idx)
