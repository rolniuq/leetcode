class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, v: int):
        self.head = v

    def middle_of_linked_list(self) -> int:
        return 0
