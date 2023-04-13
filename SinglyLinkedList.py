class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def add_at_tail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_at_head(self):
        if not self.head:
            return None
        else:
            temp = self.head
            self.head = temp.next
            return temp.val

    def delete_at_tail(self):
        if not self.head:
            return None
        elif not self.head.next:
            temp = self.head
            self.head = None
            return temp.val
        else:
            current = self.head
            while current.next.next:
                current = current.next
            temp = current.next
            current.next = None
            return temp.val

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()

    def get_length(self):
        """
        Returns the length of the linked list.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def get_node(self, index):
        """
        Returns the node at the given index in the linked list.
        """
        if index < 0 or index >= self.get_length():
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def add_at_index(self, index, val):
        """
        Adds a node with the given value at the given index in the linked list.
        """
        if index < 0 or index > self.get_length():
            return
        if index == 0:
            self.add_at_head(val)
        else:
            prev_node = self.get_node(index - 1)
            new_node = ListNode(val)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def delete_at_index(self, index):
        """
        Deletes the node at the given index in the linked list.
        """
        if index < 0 or index >= self.get_length():
            return None
        if index == 0:
            return self.delete_at_head()
        else:
            prev_node = self.get_node(index - 1)
            temp = prev_node.next
            prev_node.next = temp.next
            return temp.val


if __name__ == "__main__":
    # Create a new linked list
    my_list = LinkedList()

    # Add nodes to the list
    my_list.add_at_tail(1)
    my_list.add_at_tail(2)
    my_list.add_at_head(0)
    my_list.add_at_index(2, 5)

    # Print the list
    my_list.print_list()  # Output: 0 1 5 2

    # Delete nodes from the list
    my_list.delete_at_tail()
    my_list.delete_at_head()
    my_list.delete_at_index(1)

    # Print the list again
    my_list.print_list()  # Output: 5

    # Test the get_node method
    print(my_list.get_node(0).val)  # Output: 5

    # Test the get_length method
    print(my_list.get_length())  # Output: 1










