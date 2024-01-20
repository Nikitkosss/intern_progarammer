class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularBuffer2:
    def __init__(self, size):
        self.size = size
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Buffer is full")
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        item = self.head.value
        self.head = self.head.next
        self.count -= 1
        return item


"""
Плюсы:
- Лучшая эффективность по памяти.
В реализации с использованием связного списка,
память выделяется только при поступлении новых элементов в буфер,
что позволяет эффективно использовать ресурсы.
- Гибкость изменения размера буфера.
В связном списке можно легко изменять размер буфера,
просто изменяя переменную size.

Минусы:
- Более сложная реализация.
Исползование связного списка требует более сложного кода,
чем использование встроенного списка.
- Операции enqueue и dequeue выполняются за O(1) в среднем,
но в худшем случае может потребоваться O(n) времени,
если точка вставки/удаления наход
"""
