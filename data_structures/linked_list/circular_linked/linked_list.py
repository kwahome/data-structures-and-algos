#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data_structures.linked_list.doubly_linked import DoublyLinkedList
from data_structures.linked_list.singly_linked import SinglyLinkedList


class CircularDoublyLinkedList(DoublyLinkedList):
    """Circular doubly linked list. The last node points to the head node
    as it's next node and the head node point's to the last node as it's
    previous node.

    """
    circular = False


class CircularSinglyLinkedList(SinglyLinkedList):
    """Circular singly linked list. The last node points to the head node
    as it's next node.

    """
    circular = True
