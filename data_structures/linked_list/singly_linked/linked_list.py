#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_structures.linked_list import BaseNode, InsertPositions, LinkedList, SearchPositions


class Node(BaseNode):
    """Class implementing a `node` in a singly linked list

    Each node contains following parts:
        - value
        - a pointer to the next node
    """
    pass


class SinglyLinkedList(LinkedList):
    """Singly linked list that can only be traversed in a forward direction.

    """
    def _insert_before(self, data, reference_value):
        """Method to insert a node before the node with the `reference_value` in the linked list.

        This implementation of insert has a worst case complexity O(n). This is because the insert
        method has to first seek the position of the reference value before performing an insert. At
        best, the reference value is the head of the list and at worst it's the last item.

        :param data: data item to be inserted into the linked list
        :param reference_value: reference value for inserting between nodes
        :return:
        """
        new_node = Node(data=data)

        #: if linked list is empty, reference_value won't exist hence set new_node as head
        if self.is_empty():
            self.set_head(new_node)
            return

        node_before = self.search(data=reference_value, position=SearchPositions.BEFORE)
        if node_before:
            #: if node with reference_value is found, set new_node as it's next node
            new_node.set_next(node_before.get_next())
            node_before.set_next(new_node)
        else:
            #: if node with reference_value is not found, default to inserting to the front of the
            #: linked list as it's a constant time operation
            self.insert(data, position=InsertPositions.BEGINNING)

    def _insert_after(self, data, reference_value):
        """Method to insert a node after the node with the `reference_value` in the linked list.

        This implementation of insert has a worst case complexity O(n). This is because the insert
        method has to first seek the position of the reference value before performing an insert.
        At best, the reference value is the head of the list and at worst it's the last item.

        :param data: data item to be inserted into the linked list
        :param reference_value: reference value for inserting between nodes
        :return:
        """
        new_node = Node(data=data)

        #: if linked list is empty, reference_value won't exist hence set new_node as head
        if self.is_empty():
            self.set_head(new_node)
            return

        reference_node = self.search(data=reference_value)
        if reference_node:
            #: if node with reference_value is found, set new_node as it's next node
            new_node.set_next(reference_node.get_next())
            reference_node.set_next(new_node)
        else:
            #: if node with reference_value is not found, default to inserting to the front of the
            #: linked list as it's a constant time operation
            self.insert(data, position=InsertPositions.BEGINNING)

    def _insert_beginning(self, data, reference_value=None):
        """Method to insert a node at the beginning of the linked list

        This implementation of insert is constant O(1) (efficient!). This is because the insert
        method, no matter what, will always take the same amount of time: it can only take one data
        point, it can only ever create one node, and the new node does not need to interact with all
        the other nodes in the list, the inserted node will only ever interact with the head.

        :param data: data item to be inserted into the linked list
        :param reference_value: reference value for inserting between nodes
        :return:
        """
        new_node = Node(data=data)
        new_node.set_next(self.get_head())
        self.set_head(new_node)

    def _insert_end(self, data, reference_value=None):
        """Method to insert a node at the end of the linked list.

        This implementation of insert has a complexity O(n). This is because the insert method has
        to first seek the last node before performing an insert which would involve traversing the
        size of linked list.

        :param data: data item to be inserted into the linked list
        :param reference_value: reference value for inserting between nodes
        :return:
        """
        new_node = Node(data=data)
        if not self.head:
            self.set_head(new_node)
            return

        last_node = self.head
        #: seek the last node in the linked list first
        while last_node.get_next():
            last_node = last_node.get_next()
        last_node.set_next(new_node)

    def insert(self, data, position=InsertPositions.BEGINNING, reference_value=None):
        """Method to positionally insert a node into the linked list.

        A node can be inserted at the beginning, end, after or before a particular node.

        The default behaviour is to insert at the beginning because that implementation is of
        constant time complexity O(1).

        :param data: data item to be inserted into the linked list
        :param position: where in the linked list to do the insert i.e beginning, end, after, before
        :param reference_value: reference value for inserting between nodes i.e. after or before
        :return:
        """
        getattr(self, "_insert_{}".format(position), self._insert_beginning)(data, reference_value)

    def push(self, data):
        """Method to insert a node at the beginning of a linked list; hence the semantics.

        :param data: data item to be inserted into the linked list
        :return:
        """
        self.insert(data, position=InsertPositions.BEGINNING)

    def append(self, data):
        """Method to insert a node at the end of a linked list; hence the semantics.

        :param data: data item to be inserted into the linked list
        :return:
        """
        self.insert(data, position=InsertPositions.END)

    def _node_before(self, data):
        """Method to traverse through a linked list whilst looking for the node with the data item
        then determine the node pointing to it i.e node before it.

        Search is linear beginning at the head of the linked list thus in the event a data item
        appears more than once in the list, the first encountered is referenced.

        Search is actually very similar to size, but instead of traversing the whole list of nodes
        it checks at each stop to see whether the current node has the requested data.

        The time complexity of search is O(n) in the worst case.

        :param data: item to look for in the linked list
        :return: node after the node holding the data item
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

        #: if data item was not found, there's no previous node for it as it's not in the list
        if not found:
            previous = None
        return previous

    def _node_with(self, data):
        """Method to traverse through a linked list whilst looking for an item.

        Search is linear beginning at the head of the linked list thus in the event a data item
        appears more than once in the list, the first encountered is referenced.

        Search is actually very similar to size, but instead of traversing the whole list of nodes
        it checks at each stop to see whether the current node has the requested data.

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

    def _node_after(self, data):
        """Method to traverse through a linked list whilst looking for the node with the data item
        then determine the node it points to i.e node after it.

        Search is linear beginning at the head of the linked list thus in the event a data item
        appears more than once in the list, the first encountered is referenced.

        Search is actually very similar to size, but instead of traversing the whole list of nodes
        it checks at each stop to see whether the current node has the requested data.

        The time complexity of search is O(n) in the worst case.

        :param data: item to look for in the linked list
        :return: node after the node holding the data item
        """
        return self._node_with(data).get_next()

    def search(self, data, position=SearchPositions.CURRENT):
        """Method to traverse through a linked list whilst looking for an item.

        This method returns either the node holding the data item, the node before or the node after
        depending on the configuration chosen. It defaults to returning the node holding the item.

        Search is linear beginning at the head of the linked list thus in the event a data item
        appears more than once in the list, the first encountered is referenced.

        Search is actually very similar to size, but instead of traversing the whole list of nodes
        it checks at each stop to see whether the current node has the requested data.

        The time complexity of search is O(n) in the worst case.

        :param data: item to look for in the linked list
        :param position: node relative to the node holding data item to return
        :return: node holding the data item
        """
        return getattr(self, "_node_{}".format(position), self._node_with)(data)

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
