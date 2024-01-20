class CircularBuffer1:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * self.size
        self.head = 0
        self.tail = 0
        self.is_full = False

    def is_empty(self):
        return self.head == self.tail and not self.is_full

    def enqueue(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size
        if self.tail == self.head:
            self.is_full = True

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.size
        self.is_full = False
        return item


"""
Плюсы:
- Простота реализации. Использование встроенного
списка позволяет легко создать и управлять циклическим буфером.
- Операции enqueue и dequeue выполняются за O(1) времени.
Вставка и удаление элемента происходят за постоянное время благодаря
операции взятия остатка от деления в методах enqueue и dequeue.

Минусы:
- Потеря памяти при расширении.
При использовании списка в реализации будет зарезервирована память
для всего буфера заранее, который может быть недостаточно использованным при
небольшом количестве элементов в буфере. Это приводит к потере памяти.
- Возможность переполнения. В данной реализации можно производить вставку
элементов в буфер даже после его переполнения,
что может изменить или утерять ранее вставленные элементы.
"""
