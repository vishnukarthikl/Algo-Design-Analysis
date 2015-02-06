def quick_sort(numbers, start, end, pivot_chooser):
    if start < end:
        pivot_index = pivot_chooser(numbers, start, end)
        numbers[start], numbers[pivot_index] = numbers[pivot_index], numbers[start]
        pivot = numbers[start]
        i = start
        for j in range(start, end + 1):
            if numbers[j] < pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]

        numbers[start], numbers[i] = numbers[i], numbers[start]
        return (end - start) + quick_sort(numbers, start, i - 1, pivot_chooser) + quick_sort(numbers, i + 1, end,
                                                                                             pivot_chooser)
    else:
        return 0


def find_median_index(numbers, start, end):
    first = numbers[start], start
    last = numbers[end], end
    mid_index = (end - start) / 2 + start
    middle = numbers[mid_index], mid_index
    pivot_candidates = [first, middle, last]
    pivot_candidates.sort()
    return pivot_candidates[1][1]


contents = file.read(file('QuickSort.txt'))
numbers = contents.split('\r\n')
del numbers[-1]

numbers = map(lambda x: int(x), numbers)
n1 = list(numbers)
n2 = list(numbers)
n3 = list(numbers)
# numbers = [2, 1, 4, 5, 6, 0]
print quick_sort(n1, 0, len(n1) - 1, lambda _, start, end: start)
print quick_sort(n2, 0, len(n2) - 1, lambda _, start, end: end)
print quick_sort(n3, 0, len(n3) - 1, find_median_index)


