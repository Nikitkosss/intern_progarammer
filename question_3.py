def sort_array(arr):
    return sorted(arr)


"""
Одним из самых быстрых алгоритмов сортировки на языке Python
является алгоритм Timsort, который является комбинацией
сортировки вставками и сортировки слиянием.

Алгоритм Timsort соответствует заданным критериям по нескольким причинам:

1. Эффективность времени выполнения: Timsort имеет время выполнения O(n log n)
в худшем и среднем случае. Это означает, что время сортировки увеличивается
линейно с ростом размера массива.
2. Устойчивость: Timsort сохраняет порядок равных элементов из исходного
массива, что делает его устойчивым алгоритмом сортировки.
3. Эффективность использования памяти: Timsort использует дополнительную
память для слияния временных подмассивов, но общий объем использованной
памяти ограничен и зависит от размера массива и доступной оперативной памяти.
4. Обработка предварительно отсортированных массивов: Timsort эффективно
обрабатывает уже отсортированные или почти отсортированные массивы.
Это достигается использованием сортировки вставками для небольших подмассивов.
Функция sorted() сортирует массив arr и возвращает новый отсортированный
массив, не меняя исходного массива. Алгоритм Timsort, который используется
внутри функции sorted(), покрывает все условия, указанные выше.
"""