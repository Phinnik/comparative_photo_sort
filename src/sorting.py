from typing import Optional


class Sorter:
    def __init__(self, array: list) -> None:
        self.array = array

    def _is_greater(self, left, right) -> bool:
        # TODO: make abstract
        return left > right

    def _merge(self, left_idx: int, mid_idx: int, right_idx: int):
        left_array = self.array[left_idx : mid_idx + 1]
        right_array = self.array[mid_idx + 1 : right_idx + 1]

        i, j = 0, 0
        k = left_idx

        while (i < len(left_array)) and (j < len(right_array)):
            if self._is_greater(left_array[i], right_array[j]):
                self.array[k] = right_array[j]
                j += 1
            else:
                self.array[k] = left_array[i]
                i += 1
            k += 1

        while i < len(left_array):
            self.array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            self.array[k] = right_array[j]
            j += 1
            k += 1

    def sort(
        self,
        left_idx: Optional[int] = None,
        right_idx: Optional[int] = None,
    ):
        left_idx = left_idx if left_idx is not None else 0
        right_idx = right_idx if right_idx is not None else len(self.array) - 1

        if left_idx < right_idx:
            mid_idx = left_idx + (right_idx - left_idx) // 2

            self.sort(left_idx, mid_idx)
            self.sort(mid_idx + 1, right_idx)
            self._merge(left_idx, mid_idx, right_idx)
