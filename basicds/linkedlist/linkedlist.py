import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import node


class LinkedList():
    def __init__(self):
        self.root = node.Node(val=0)
        self.len = 0

    def __str__(self):
        temp = self.root
        result = ""
        while temp != None:
            result += str(temp.val) + "->"
            temp = temp.next
        return result

    def insert_at(self, e, at):  # insert element (e) after (at)
        # at -> e
        e.next = at.next
        at.next = e
        self.len += 1

    # insert_value is wrapper of insert(Node(val: v), at)
    def insert_value(self, val, at):
        self.insert_at(node.Node(val=val), self.root)

    def push_front(self, val):
        self.insert_value(val, self.root)


def New():
    return LinkedList()
