# QUESTION: Write a function to reverse a linked list


class Node:
    """Node"""

    def __init__(self, a_number):
        self.data = a_number
        self.next = None


class LinkedList:
    """Linked list"""

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


def reverse(l):
    if l.head is None:
        return

    current_node = l.head
    prev_node = None

    while current_node is not None:
        # Track the next node
        next_node = current_node.next

        # Modify the current node
        current_node.next = prev_node

        # Update prev and current
        prev_node = current_node
        current_node = next_node

    l.head = prev_node


list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

# print(list2.length())
print(list2.show_elements())
reverse(list2)
print(list2.show_elements())
