# Implement "reverse" as a method of SinglyLinkedList, called as L.reverse(),
# that reverses the SinglyLinkedList instance L
# using only a constant amount of additional space and not using any recursion.
from random import randint


class SinglyLinkedList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
        def __str__(self):
            return str(self._element)

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        self._head = self._Node(e, self._head)
        if self.is_empty():
            self._tail = self._head
        self._size += 1

    def add_last(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            self._head = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def remove_last(self):
        if self.is_empty():
            raise Exception('Linked list is empty')
        if self._size == 1:
            answer = self._head._element
            self._head = None
            self._tail = None
        else:
            answer = self._tail._element
            current_node = self._head
            next_node = current_node._next
            while next_node != self._tail:
                current_node = next_node
                next_node = next_node._next
            self._tail = current_node
        self._size -= 1
        return answer

#reverse the linked list
    def reverse(self):
        #swap head and tail
        self._head, self._tail = self._tail, self._head
        #temp points to tail node
        temp = self._tail
        #current points to node after temp
        curr = temp._next
        #while the current link doesn't equal None
        while curr != None:
            #next points to node after current
            next = curr._next
            #flip current and temp
            curr._next = temp
            #temp points to current
            temp = curr
            #current points to next
            curr = next
        #set node after tail to None
        self._tail._next = None



    def __str__(self):
        temp = self._head
        s = ""
        while temp != None:
            s += f"{temp}-"
            temp = temp._next
        return s


if __name__ == "__main__":
    L = SinglyLinkedList()
    for i in range(10):
        L.add_last(randint(0, 10))
    print(L)
    L.reverse()
    print(L)
