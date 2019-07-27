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

    def __init__(self, data=None, previous_node=None, next_node=None):
        super(Node, self).__init__(data=data, next_node=next_node)
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

    A doubly linked list could also be circularly linked where the last node
    points to the head node as it's next node and the head node point's to
    the last node as it's previous node.

    """
    circular = False  #: boolean flag indicating whether the linked list is circular

    def make_circular(self):
        """Method to circularly link a doubly linked list.

        :return:
        """
        if self.get_head():
            self.get_head().set_previous(self.get_tail())

        if self.get_tail():
            self.get_tail().set_next(self.get_head())

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

        #: if linked list is empty, reference_value won't exist hence initialize with node
        if self.is_empty():
            return self.initialize(node=new_node)

        reference_node = self.search(data=reference_value)
        if reference_node and reference_node.get_previous():
            #: if node with reference_value is found, set new_node as it's previous node
            #: no need to reset list tail as new node is inserted before another node
            #: because even in the event that that node was the tail, it will not be
            #: displaced from it's position
            node_before = reference_node.get_previous()
            new_node.set_next(reference_node)
            new_node.set_previous(node_before)
            reference_node.set_previous(new_node)
            node_before.set_next(new_node)
            if reference_node is self.get_head():
                self.set_head(new_node)
        else:
            #: if node with reference_value is not found, default to inserting to the front of the
            #: linked list as it's a constant time operation
            #: also if the reference node is the head of the linked list
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
        #: if linked list is empty, reference_value won't exist hence initialize with node
        if self.is_empty():
            return self.initialize(node=new_node)

        reference_node = self.search(data=reference_value)
        if reference_node:
            #: if node with reference_value is found, set new_node as it's next node
            new_node.set_next(reference_node.get_next())
            new_node.set_previous(reference_node)
            next_node = reference_node.get_next()
            if next_node:
                next_node.set_previous(new_node)
            reference_node.set_next(new_node)

            #: we need to reset the list's tail as new node is inserted after the reference
            #: node which is displaced from it's position as the last node in the list
            if reference_node is self.get_tail():
                self.set_tail(new_node)
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
        #: create node with data
        new_node = Node(data=data)
        #: set next to point to the current head
        new_node.set_next(self.get_head())
        #: change previous of current head node to point to the new node
        if not self.is_empty():
            self.head.set_previous(new_node)
        #: set the new node as the head of the list
        self.set_head(new_node)

        #: set the tail of the list if it was an empty list
        if not self.get_tail() or not self.get_head().get_next():
            self.set_tail(new_node)

    def _insert_end(self, data, reference_value=None):
        """Method to insert a node at the end of the linked list.

        This implementation of insert has a complexity O(n). This is because the insert method has
        to first seek the last node before performing an insert which would involve traversing the
        size of linked list.

        :param data: data item to be inserted into the linked list
        :param reference_value: reference value for inserting between nodes
        :return:
        """
        #: create node with data
        new_node = Node(data=data)
        #: if linked list is empty, reference_value won't exist hence initialize with node
        if self.is_empty():
            return self.initialize(node=new_node)
        tail = self.get_tail()
        new_node.set_previous(tail)
        tail.set_next(new_node)
        #: set new node as the tail of the list
        self.set_tail(new_node)

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
        getattr(self, "_insert_{}".format(position.lower()), self._insert_beginning)(
            data, reference_value
        )
        #: since this is the entry point for all inserts; push, append, insert before and after,
        #: we want to control the list's circular property on insert from this point by setting
        #: the tail node's next pointer to the head node after every insert operation and the
        #: head node's
        if self.circular:
            self.make_circular()

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
        current = self._node_with(data)
        previous_node = None
        if current:
            previous_node = current.get_previous()
        return previous_node

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

        head = self.get_head()
        current, found, result = head, False, None
        #: while taking care to ensure that we are not circling back
        #: in a circular linked list hence iterating infinitely
        while not found and current:
            if current.get_data() == data:
                result, found = current, True
                break
            previous, current = current, current.get_next()
            #: how we know we have circled back in a circular linked list
            if not found and current is head:
                current = None
        return result

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
        current = self._node_with(data)
        next_node = None
        if current:
            next_node = current.get_next()
        return next_node

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
        return getattr(self, "_node_{}".format(position.lower()), self._node_with)(data)

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
        previous = None
        node = self.search(data)
        if node:
            previous = node.get_previous()

        #: can't delete a node if it does not exist
        if not node:
            return

        next_node = node.get_next()
        if node == next_node:
            self.set_head(None)
            self.set_tail(None)
            return

        if previous:
            previous.set_next(next_node)

        if not previous or node is self.get_head():
            self.set_head(next_node)

        if node and next_node:
            next_node.set_previous(previous)

        #: if we have just deleted the last node
        if not next_node or node is self.get_tail():
            self.set_tail(previous)

        #: since this is the entry point for all delete operations we want to control the list's
        #: circular property on deletion from this point by setting the tail node's next pointer
        # to the head node after every delete operation
        if self.circular:
            self.make_circular()
