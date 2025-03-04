import time
import logging
import unittest
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Функция {func.__name__} выполнялась {execution_time:.4f} секунд")
        return result
    return wrapper

def log_calls(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args] 
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] 
        signature = ", ".join(args_repr + kwargs_repr)
        logging.info(f"Вызов функции {func.__name__}({signature})")
        result = func(*args, **kwargs)
        logging.info(f"Функция {func.__name__} вернула: {result!r}")
        return result
    return wrapper


@timeit
@log_calls
def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n) - 1 - i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j + 1], n[j]
    return n

@timeit
@log_calls
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i
        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1
        array[j] = x
    return array

class TestSortingAlgorithms(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(insertion_sort([]), [])

    def test_already_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_random_list(self):
        random_list = [random.randint(1, 100) for _ in range(20)]  # Создаем список случайных чисел
        expected_sorted = sorted(random_list)
        self.assertEqual(bubble_sort(random_list.copy()), expected_sorted)
        self.assertEqual(insertion_sort(random_list.copy()), expected_sorted)

    def test_negative_numbers(self):
         self.assertEqual(bubble_sort([-5, -2, 0, -8, 3]), [-8, -5, -2, 0, 3])
         self.assertEqual(insertion_sort([-5, -2, 0, -8, 3]), [-8, -5, -2, 0, 3])

    def test_mixed_numbers(self):
        self.assertEqual(bubble_sort([-1, 0, 1, -2, 2]), [-2, -1, 0, 1, 2])
        self.assertEqual(insertion_sort([-1, 0, 1, -2, 2]), [-2, -1, 0, 1, 2])
if __name__ == '__main__':
    unittest.main()