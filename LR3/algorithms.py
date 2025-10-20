import logging
import random
from LR3.data import Data

# Настройка логирования для алгоритмов
algorithm_logger = logging.getLogger('algorithms')


def bubble_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_bubble_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    swap = True
    count_iteration = 0
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                algorithm_logger.info(
                    f"Number {nums[i]}({i}-th position) is greater than {nums[i + 1]}({i + 1}-th position). Swapping them!")

                # Highlight elements being swapped
                for d in frames[-1]:
                    d.set_color('#1f77b4')
                frames[-1][i].set_color('#ff0000')
                frames[-1][i + 1].set_color('#ff0000')

                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                new_frame = [Data(d.value) for d in frames[-1]]
                new_frame[i].value = nums[i]
                new_frame[i + 1].value = nums[i + 1]
                new_frame[i].set_color('#00ff00')
                new_frame[i + 1].set_color('#00ff00')
                frames.append(new_frame)
                swap = True
            count_iteration += 1

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration}")
    return frames


def selection_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_selection_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    count_iteration = 0
    for i in range(len(nums)):
        low_num = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[low_num]:
                low_num = j
            count_iteration += 1

        algorithm_logger.info(
            f"Found smallest number {nums[low_num]}({low_num}-th position), swapping it with {nums[i]}({i}-th position)!")

        # Highlight elements being swapped
        for d in frames[-1]:
            d.set_color('#1f77b4')
        frames[-1][i].set_color('#ff0000')
        frames[-1][low_num].set_color('#ff0000')

        nums[i], nums[low_num] = nums[low_num], nums[i]
        new_frame = [Data(d.value) for d in frames[-1]]
        new_frame[i].value = nums[i]
        new_frame[low_num].value = nums[low_num]
        new_frame[i].set_color('#00ff00')
        new_frame[low_num].set_color('#00ff00')
        frames.append(new_frame)

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration}")
    return frames


def insertion_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_insertion_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    count_iteration = 0
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        count_iteration += 1

        while j >= 0 and nums[j] > item_to_insert:
            algorithm_logger.info(f"Moving element {nums[j]}({j}-th position) to position {j + 1}")

            # Highlight moving element
            for d in frames[-1]:
                d.set_color('#1f77b4')
            frames[-1][j].set_color('#ff0000')
            frames[-1][j + 1].set_color('#ff0000')

            nums[j + 1] = nums[j]
            new_frame = [Data(d.value) for d in frames[-1]]
            new_frame[j + 1].value = nums[j + 1]
            new_frame[j].set_color('#00ff00')
            new_frame[j + 1].set_color('#00ff00')
            frames.append(new_frame)
            j -= 1
            count_iteration += 1

        algorithm_logger.info(f"Inserting element {item_to_insert} into position {j + 1}")
        nums[j + 1] = item_to_insert
        new_frame = [Data(d.value) for d in frames[-1]]
        new_frame[j + 1].value = item_to_insert
        new_frame[j + 1].set_color('#00ff00')
        frames.append(new_frame)

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration}")
    return frames


def heapify(nums, heap_size, root_index, count_iteration, frames, current_frame):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    count_iteration[0] += 1
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    count_iteration[0] += 1
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    count_iteration[0] += 1
    if largest != root_index:
        algorithm_logger.info(
            f"Swapping root {nums[root_index]}({root_index}) with largest child {nums[largest]}({largest})")

        # Highlight swap
        for d in current_frame:
            d.set_color('#1f77b4')
        current_frame[root_index].set_color('#ff0000')
        current_frame[largest].set_color('#ff0000')

        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        new_frame = [Data(d.value) for d in current_frame]
        new_frame[root_index].value = nums[root_index]
        new_frame[largest].value = nums[largest]
        new_frame[root_index].set_color('#00ff00')
        new_frame[largest].set_color('#00ff00')
        frames.append(new_frame)

        heapify(nums, heap_size, largest, count_iteration, frames, new_frame)


def heap_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_heap_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")
    algorithm_logger.info("Building Max Heap from list")

    n = len(nums)
    count_iteration = [0]

    for i in range(n, -1, -1):
        heapify(nums, n, i, count_iteration, frames, frames[-1])

    algorithm_logger.info("Extracting elements from heap")
    for i in range(n - 1, 0, -1):
        algorithm_logger.info(f"Moving root {nums[0]} to position {i}, swapping with {nums[i]}")

        # Highlight swap
        for d in frames[-1]:
            d.set_color('#1f77b4')
        frames[-1][0].set_color('#ff0000')
        frames[-1][i].set_color('#ff0000')

        nums[i], nums[0] = nums[0], nums[i]
        new_frame = [Data(d.value) for d in frames[-1]]
        new_frame[i].value = nums[i]
        new_frame[0].value = nums[0]
        new_frame[i].set_color('#00ff00')
        new_frame[0].set_color('#00ff00')
        frames.append(new_frame)

        heapify(nums, i, 0, count_iteration, frames, new_frame)

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration[0]}")
    return frames


def merge(left_list, right_list, count_iteration, frames, current_frame):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        count_iteration[0] += 1
        if left_list_index < left_list_length and right_list_index < right_list_length:
            count_iteration[0] += 1
            if left_list[left_list_index] <= right_list[right_list_index]:
                algorithm_logger.info(f"Adding element {left_list[left_list_index]} from left list to sorted result")
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                algorithm_logger.info(f"Adding element {right_list[right_list_index]} from right list to sorted result")
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            algorithm_logger.info(
                f"Reached end of left list, adding remaining element {right_list[right_list_index]} from right list")
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            algorithm_logger.info(
                f"Reached end of right list, adding remaining element {left_list[left_list_index]} from left list")
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    # Create new frame for merged result
    new_frame = [Data(d.value) for d in current_frame]
    for i in range(len(sorted_list)):
        new_frame[i].value = sorted_list[i]
        new_frame[i].set_color('#00ff00')
    frames.append(new_frame)

    return sorted_list


def merge_sort_helper(nums, count_iteration, frames, current_frame):
    count_iteration[0] += 1
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    algorithm_logger.info(f"Splitting list into left: {nums[:mid]} and right: {nums[mid:]}")

    left_list = merge_sort_helper(nums[:mid], count_iteration, frames, current_frame)
    right_list = merge_sort_helper(nums[mid:], count_iteration, frames, current_frame)

    algorithm_logger.info(f"Merging left list {left_list} with right list {right_list}")
    return merge(left_list, right_list, count_iteration, frames, current_frame)


def merge_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_merge_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    count_iteration = [0]
    sorted_nums = merge_sort_helper(nums, count_iteration, frames, frames[-1])

    algorithm_logger.info(f"Sorted list: {sorted_nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration[0]}")
    return frames


def partition(nums, low, high, count_iteration, frames, current_frame):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1

    algorithm_logger.info(f"Partitioning from index {low} to {high}, pivot element: {pivot}")

    while True:
        i += 1
        count_iteration[0] += 1
        while nums[i] < pivot:
            count_iteration[0] += 1
            i += 1

        j -= 1
        count_iteration[0] += 1
        while nums[j] > pivot:
            count_iteration[0] += 1
            j -= 1

        count_iteration[0] += 1
        if i >= j:
            algorithm_logger.info(f"Partition complete, split index: {j}")
            return j

        algorithm_logger.info(f"Swapping elements {nums[i]}(index {i}) and {nums[j]}(index {j})")

        # Highlight swap
        for d in current_frame:
            d.set_color('#1f77b4')
        current_frame[i].set_color('#ff0000')
        current_frame[j].set_color('#ff0000')

        nums[i], nums[j] = nums[j], nums[i]
        new_frame = [Data(d.value) for d in current_frame]
        new_frame[i].value = nums[i]
        new_frame[j].value = nums[j]
        new_frame[i].set_color('#00ff00')
        new_frame[j].set_color('#00ff00')
        frames.append(new_frame)


def quick_sort_helper(nums, low, high, count_iteration, frames, current_frame):
    count_iteration[0] += 1
    if low < high:
        algorithm_logger.info(f"Recursively sorting partition [{low}, {high}]")
        split_index = partition(nums, low, high, count_iteration, frames, current_frame)

        algorithm_logger.info(f"Recursively sorting left partition [{low}, {split_index}]")
        quick_sort_helper(nums, low, split_index, count_iteration, frames, frames[-1])

        algorithm_logger.info(f"Recursively sorting right partition [{split_index + 1}, {high}]")
        quick_sort_helper(nums, split_index + 1, high, count_iteration, frames, frames[-1])


def quick_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_quick_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    count_iteration = [0]
    quick_sort_helper(nums, 0, len(nums) - 1, count_iteration, frames, frames[-1])

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration[0]}")
    return frames


def shell_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_shell_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    count_iteration = 0
    n = len(nums)
    gap = n // 2

    while gap > 0:
        algorithm_logger.info(f"Current gap: {gap}")
        for i in range(gap, n):
            temp = nums[i]
            j = i
            count_iteration += 1

            while j >= gap and nums[j - gap] > temp:
                algorithm_logger.info(f"Moving element {nums[j - gap]}({j - gap}) to position {j}")

                # Highlight moving element
                for d in frames[-1]:
                    d.set_color('#1f77b4')
                frames[-1][j - gap].set_color('#ff0000')
                frames[-1][j].set_color('#ff0000')

                nums[j] = nums[j - gap]
                new_frame = [Data(d.value) for d in frames[-1]]
                new_frame[j].value = nums[j]
                new_frame[j - gap].set_color('#00ff00')
                new_frame[j].set_color('#00ff00')
                frames.append(new_frame)

                j -= gap
                count_iteration += 1

            nums[j] = temp
            new_frame = [Data(d.value) for d in frames[-1]]
            new_frame[j].value = temp
            new_frame[j].set_color('#00ff00')
            frames.append(new_frame)

        gap //= 2

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration}")
    return frames


def comb_sort(data_set):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_comb_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")

    count_iteration = 0
    n = len(nums)
    gap = n
    swapped = True
    shrink_factor = 1.3

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        algorithm_logger.info(f"Current gap: {gap}")
        swapped = False

        for i in range(n - gap):
            count_iteration += 1
            if nums[i] > nums[i + gap]:
                algorithm_logger.info(f"Swapping elements {nums[i]}({i}) and {nums[i + gap]}({i + gap}) with gap {gap}")

                # Highlight swap
                for d in frames[-1]:
                    d.set_color('#1f77b4')
                frames[-1][i].set_color('#ff0000')
                frames[-1][i + gap].set_color('#ff0000')

                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                new_frame = [Data(d.value) for d in frames[-1]]
                new_frame[i].value = nums[i]
                new_frame[i + gap].value = nums[i + gap]
                new_frame[i].set_color('#00ff00')
                new_frame[i + gap].set_color('#00ff00')
                frames.append(new_frame)
                swapped = True

    algorithm_logger.info(f"Sorted list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration}")
    return frames


def monkey_sort(data_set, max_frames=100):
    nums = [d.value for d in data_set]
    frames = [data_set.copy()]

    algorithm_logger.info("------ Start_monkey_sort - logging ------")
    algorithm_logger.info(f"Initial list: {nums}")
    algorithm_logger.info("Monkey sort: randomly shuffling until sorted")

    count_iteration = 0
    max_iterations = min(max_frames, 1000)  # Limit iterations

    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    while not is_sorted(nums) and count_iteration < max_iterations:
        count_iteration += 1
        algorithm_logger.info(f"Shuffle attempt {count_iteration}")

        # Highlight shuffle
        for d in frames[-1]:
            d.set_color('#1f77b4')

        random.shuffle(nums)
        new_frame = [Data(d.value) for d in frames[-1]]
        for i in range(len(nums)):
            new_frame[i].value = nums[i]
            new_frame[i].set_color('#ff0000')
        frames.append(new_frame)

        if count_iteration % 10 == 0:
            algorithm_logger.info(f"Still shuffling... attempt {count_iteration}")

    if is_sorted(nums):
        algorithm_logger.info(f"Successfully sorted after {count_iteration} shuffles")
        # Final sorted frame
        new_frame = [Data(d.value) for d in frames[-1]]
        for i in range(len(nums)):
            new_frame[i].value = nums[i]
            new_frame[i].set_color('#00ff00')
        frames.append(new_frame)
    else:
        algorithm_logger.info(f"Stopped after {count_iteration} shuffles (not sorted)")

    algorithm_logger.info(f"Final list: {nums}")
    algorithm_logger.info(f"Iteration count: {count_iteration}")
    return frames