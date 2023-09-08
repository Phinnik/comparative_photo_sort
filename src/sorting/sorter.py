from typing import Optional


class Sorter:
    def __init__(self, array: list) -> None:
        self.array = array
        self.indices = list(range(len(array)))

    def _is_greater(self, left, right) -> bool:
        # TODO: make abstract
        return left > right

    def _merge(self, start_idx: int, mid_idx: int, end_idx: int):
        left_indices = self.indices[start_idx : mid_idx + 1]
        right_indices = self.indices[mid_idx + 1 : end_idx + 1]

        i, j = 0, 0
        k = start_idx

        while (i < len(left_indices)) and (j < len(right_indices)):
            left_index, right_index = left_indices[i], right_indices[j]
            left_value = self.array[left_index]
            right_value = self.array[right_index]
            if self._is_greater(left_value, right_value):
                self.indices[k] = right_index
                j += 1
            else:
                self.indices[k] = left_index
                i += 1
            k += 1

        while i < len(left_indices):
            self.indices[k] = left_indices[i]
            i += 1
            k += 1

        while j < len(right_indices):
            self.indices[k] = right_indices[j]
            j += 1
            k += 1

    def sort(
        self,
        start_idx: Optional[int] = None,
        end_idx: Optional[int] = None,
    ) -> list:
        start_idx = start_idx if start_idx is not None else 0
        end_idx = end_idx if end_idx is not None else len(self.array) - 1

        if start_idx < end_idx:
            mid_idx = start_idx + (end_idx - start_idx) // 2

            self.sort(start_idx, mid_idx)
            self.sort(mid_idx + 1, end_idx)
            self._merge(start_idx, mid_idx, end_idx)

        sorted_list = [self.array[i] for i in self.indices]
        return sorted_list
