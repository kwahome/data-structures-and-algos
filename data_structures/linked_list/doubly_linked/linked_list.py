#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_structures.linked_list import BaseNode, InsertPositions, LinkedList, SearchPositions


class Node(BaseNode):
    """Class implementing a `node` in a linked list

    Each node contains following parts:
        - value
        - a pointer to the previous node
        - a pointer to the next node
    """

    def __init__(self, data=None, previous_node=None, next_node=None ):
        super(Node).__init__(data=data, next_node=next_node)
        self.previous = previous_node

    def get_previous(self):
        """Getter for next node pointed at.

        :return: next node
        """
        return self.previous

    def set_previous(self, node):
        """Setter for next node to point at.

        :param node: next node
        :return:
        """
        self.previous = node


class DoublyLinkedList(LinkedList):
    """Doubly linked list that can only be traversed in a forward direction.

    """
    pass
