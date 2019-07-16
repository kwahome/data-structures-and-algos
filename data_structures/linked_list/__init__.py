#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

import abc
import six


__all__ = [
    'BaseNode',
    'InsertPositions',
    'LinkedList',
    'SearchPositions'
]

AFTER = "after"
BEFORE = "before"
BEGINNING = "beginning"
CURRENT = "with"
END = "end"


class InsertPositions:
    """Class implementing an enum construct describing linked list insertion positions.
    """
    AFTER = AFTER
    BEFORE = BEFORE
    BEGINNING = BEGINNING
    END = END


class SearchPositions:
    """Class implementing an enum construct describing linked list search positions.
    """
    AFTER = AFTER
    BEFORE = BEFORE
    CURRENT = CURRENT


class BaseNode(object):
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


class LinkedList(six.with_metaclass(abc.ABCMeta)):
    """Linked list base defining a head.

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

    def is_empty(self):
        """Method to check whether a linked list is empty.

        A linked list will be empty if it has no head as it must always start from the head.

        :return: True or False
        """
        return self.head is None

    def get_tail(self):
        """Method to seek and return the last node in the linked list (tail).

        :return: last node in the linked list
        """
        last_node = self.head
        while last_node and last_node.get_next():
            last_node = last_node.get_next()
        return last_node

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

    def to_array(self):
        """Method to traverse linked list and return an array of all it's items.

        :return: array
        """
        array = []
        current = self.head
        while current:
            array.append(current.get_data())
            current = current.get_next()
        return array

    def traverse(self):
        """Method to traverse linked list and print out all it's items.

        :return:
        """
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

    @abc.abstractmethod
    def insert(self, data, position=InsertPositions.BEGINNING, reference_value=None):
        """Method to insert data item into a chosen position in the linked list.

        :param data: data item
        :param position: where in the linked list to do the insert i.e beginning, end, after, before
        :param reference_value: reference value for inserting between nodes i.e. after or before
        :return:
        """
        pass

    @abc.abstractmethod
    def push(self, data):
        """Method to push data item to the beginning of a linked list.

        :param data: data item
        :return:
        """
        pass

    @abc.abstractmethod
    def append(self, data):
        """Method to append data item to the end of a linked list.

        :param data: data item
        :return:
        """
        pass

    @abc.abstractmethod
    def search(self, data, position=SearchPositions.CURRENT):
        """Method to search for data item in a linked list and return it's node, the node before or
        the node after as desired.

        :param data: data item
        :param position: node of interest relative to the found data item node
        :return: node of interest relative to the found data item node
        """
        pass

    @abc.abstractmethod
    def delete(self, data):
        """Method to delete data item from a linked list.

        :param data: data item.
        :return:
        """
        pass
