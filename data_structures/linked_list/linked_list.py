#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    """Class implementing a `node` in a linked list

    Each node contains following parts:
        - value
        - a pointer to the next node
    """

    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node

    def get_data(self):
        """Getter for node value.

        :return: data value
        """
        return self.value

    def set_data(self, data):
        """Setter for node value.

        :param data:
        :return:
        """
        self.value = data

    def get_next(self):
        """Getter for next node pointed at.

        :return: next node
        """
        return self.next

    def set_next(self, node):
        """Setter for next node to point at.

        :param node: next node
        :return:
        """
        self.next = node


class SinglyLinkedList(object):
    """Singly linked list that can only be traversed in a forward direction.

    """
    def __init__(self, head=None):
        self.head = head

    def get_head(self):
        """Getter for the linked list head node.

        :return: node at head
        """
        return self.head

    def set_head(self, node):
        """Setter for the linked list head node.

        :param node: node at head of linked list
        :return:
        """
        self.head = node

    def insert(self, data):
        """Method to insert a node into the linked list

        This insert method takes data, initializes a new node with the given data, and adds it to
        the list. Technically you can insert a node anywhere in the list, but the simplest way to
        do it is to place it at the head of the list and point the new node at the old head
        (sort of pushing the other nodes down the line).

        As for time complexity, this implementation of insert is constant O(1) (efficient!).
        This is because the insert method, no matter what, will always take the same amount of time:
        it can only take one data point, it can only ever create one node, and the new node does not
        need to interact with all the other nodes in the list, the inserted node will only ever
        interact with the head.

        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.set_next(self.get_head())
        self.set_head(new_node)

    def size(self):
        """Method to determine the number of nodes in a linked list.

        The size method is very simple, it basically counts nodes until it can’t find any more, and
        returns how many nodes it found. The method starts at the head node, travels down the line
        of nodes until it reaches the end (the current will be None when it reaches the end) while
        keeping track of how many nodes it has seen.

        The time complexity of size is O(n) because each time the method is called it will always
        visit every node in the list but only interact with them once, so n * 1 operations.

        :return: number of nodes found
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """Method to traverse through a linked list whilst looking for an item.

        Search is actually very similar to size, but instead of traversing the whole list of nodes
        it checks at each stop to see whether the current node has the requested data and if so,
        returns the node holding that data. If the method goes through the entire list but still
        has not found the data, it raises a value error and notifies the user that the data is not
        in the list.

        The time complexity of search is O(n) in the worst case.

        :param data: item to look for in the linked list
        :return: node holding the data item
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return current

    def delete(self, data):
        """Method to traverse through a linked list whilst looking for an item to delete it.

        Delete is very similar to search. The delete method traverses the list in the same way that
        search does, but in addition to keeping track of the current node, the delete method also
        remembers the last node it visited. When delete finally arrives at the node it wants to
        delete, it simply removes that node from the chain by “leap frogging” it. This mean that
        when the delete method reaches the node it wants to delete, it looks at the last node it
        visited (the ‘previous’ node), and resets that previous node’s pointer so that, rather than
        pointing to the soon-to-be-deleted node, it will point to the next node in line. Since no
        nodes are pointing to the poor node that is being deleted, it is effectively removed from
        the list!

        The time complexity for delete is also O(n), because in the worst case it will visit every
        node, interacting with each node a fixed number of times.

        :param data: item to delete from the linked list
        :return:
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()

        next_node = current.get_next()
        if found and next_node is not None:
            previous.set_next(current.get_next())
