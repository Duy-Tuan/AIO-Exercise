class StackList:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.__stack.pop(-1)

    def push(self, value):
        if self.is_full():
            print("Stack is full. Can not push more value")
        else:
            self.__stack.append(value)

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.__stack[-1]


if __name__ == "__main__":
    print("Exercise 9")
    print("-"*20)
    stack1 = StackList(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.is_full())

    print("\nExercise 10")
    print("-"*20)
    stack1 = StackList(capacity=5)
    stack1.push(1)
    assert stack1.is_full() == False
    stack1.push(2)
    print(stack1.top())
