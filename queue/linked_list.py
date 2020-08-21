class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        # check if there is no head
        if not self.head:
            # if list is initially empty, set head and tail to new node
            self.head = new_node
            self.tail = new_node
            # add the new node to the tail
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # if no head return none
        if not self.head:
            return None
        # if head has no next, then we have a single element in the list
        if not self.head.get_next():
            head = self.head
            self.head = None
            # delete the list's head ref
            self.tail = None
            return head.get_value()  # return the value
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.next_node = None
        return value

    def contains(self, value):
        if not self.head:
            return False

        current = self.head
        # check to see if we're at a valid node
        while current:
            if current.get_value() == value:
                return True
             # update our current node to the current node's next node
            current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()  # ref to the largest value we've seen so far
        current = self.head.get_next()
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                max_value = current.get_value()
             # update the current node to the next node in the list
            current = current.get_next()
        return max_value
