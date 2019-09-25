# selection
# merge

# назва алгоритму
# час роботи
# кількість операцій порівняння
# кількість операцій обміну
# Результати сортування

from time import time

selection_swaps = 0
selection_comparisons = 0

merge_swaps = 0
merge_comparisons = 0


class Ship:
    def __init__(self, name, reservoir, number_of_containers):
        self.name = name
        self.reservoir = reservoir
        self.number_of_containers = number_of_containers

    def __repr__(self): return "\n name: " + str(self.name) + "  reservoir: " + str(
        self.reservoir) + "  number_of_containers: " + str(self.number_of_containers) + "\n"


def selection_sort(array):
    global selection_swaps
    global selection_comparisons
    length = len(array)
    for i in range(length):
        low_idx = i
        for j in range(i + 1, length):
            selection_comparisons += 1
            if array[j].reservoir < array[low_idx].reservoir:
                low_idx = j
        array[i], array[low_idx] = array[low_idx], array[i]
        selection_swaps += 1
    return array


def merge_sort(array):
    global merge_swaps
    global merge_comparisons
    length = len(array)
    if length <= 1:
        return array
    result = []
    mid = int(length / 2)
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        merge_comparisons += 1
        if left_half[left_index].number_of_containers > right_half[right_index].number_of_containers:
            merge_comparisons += 1
            merge_swaps += 1
            result.append(left_half[left_index])
            left_index += 1
        else:
            merge_comparisons += 1
            merge_swaps += 1
            result.append(right_half[right_index])
            right_index += 1

    result += left_half[left_index:]
    result += right_half[right_index:]

    return result


s1 = Ship("ship1", 600, 4)
s2 = Ship("ship2", 300, 3)
s3 = Ship("ship3", 400, 7)
s4 = Ship("ship4", 700, 5)
s5 = Ship("ship5", 500, 6)

ship_array = [s1, s2, s3, s4, s5]


print("Seletcion Sort:\n")
start = time()
print(selection_sort(ship_array))
end = time()
comp_time = end - start
print("\nComparisons: " + str(selection_comparisons) +
      "\nSwaps: " + str(selection_swaps))
print("\nCompilation time: %.20f" % comp_time)


print("\n\nMerge Sort:\n")
start = time()
print(merge_sort(ship_array))
end = time()
comp_time = end - start
print("\nComparisons: " + str(merge_comparisons) +
      "\nSwaps: " + str(merge_swaps))
print("\nCompilation time: %.20f" % comp_time)
