from typing import NamedTuple

class Main():

    class IntegerElement(NamedTuple):
        value: int
        origIndex: int

    def two_sum(nums: list[int], target: int) -> list[int]:
        sorted_array: Main.IntegerElement = [None] * len(nums)
        for i in range(len(nums)):
            sorted_array[i] = Main.IntegerElement(nums[i], i)

        sorted_array.sort(key = lambda element: element.value) # Сортировка по лямбда компаратору

        for i in range(len(sorted_array)):
            dif = target - sorted_array[i].value
            for j in range(i + 1, len(sorted_array)):
                if sorted_array[j].value > dif:
                    break
                if sorted_array[j].value == dif:
                    return [sorted_array[i].origIndex, sorted_array[j].origIndex]

        return [0, 0]
