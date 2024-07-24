import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Пример использования всех алгоритмов
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Quick Sort:", quick_sort(arr.copy()))
    print("Selection Sort:", selection_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))

    # Визуализация сложности алгоритмов
    n = np.linspace(1, 100, 100)
    n_log_n = n * np.log2(n)
    n_squared = n**2

    plt.figure(figsize=(10, 6))

    # Bubble Sort
    plt.plot(n, n_squared, label='Bubble Sort (O(n^2))', linestyle='--')

    # Quick Sort
    plt.plot(n, n_log_n, label='Quick Sort (O(n log n))')
    plt.plot(n, n_squared, label='Quick Sort (Worst Case O(n^2))', linestyle='--')

    # Selection Sort
    plt.plot(n, n_squared, label='Selection Sort (O(n^2))', linestyle='--')

    # Insertion Sort
    plt.plot(n, n_squared, label='Insertion Sort (O(n^2))', linestyle='--')

    # Настройка графика
    plt.yscale('log')  # Логарифмическая шкала по оси Y для лучшего представления
    plt.xlabel('n (размер массива)')
    plt.ylabel('Количество операций')
    plt.title('Сложность алгоритмов сортировки')
    plt.legend()
    plt.grid(True)

    plt.show()
