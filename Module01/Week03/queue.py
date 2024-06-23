class QueueList:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full. Can not enqueue more value")
        else:
            return self.__queue.append(value)

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.__queue[0]


if __name__ == "__main__":
    print("Exercise 11")
    print("-"*20)
    queue1 = QueueList(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.is_full())

    print("\nExercise 12")
    print("-"*20)
    queue1 = QueueList(capacity=5)
    queue1.enqueue(1)
    assert queue1.is_full() == False
    queue1.enqueue(2)
    print(queue1.front())
