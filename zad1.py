from typing import Any

class Node:
    value:Any
    next: 'Node'
    def __init__(self,value,next):
        self.value=value
        self.next=next

class LinkedList:
    head:None
    tail:None
    def __init__(self):
        self.head=None
        self.tail=None
    def __str__(self):
        if self.head==None:
            return "lista jest pusta"
        else:
            ciag=""
            element=self.head
            while element!=None:
                ciag += str(element.value) + " -> "
                element=element.next
            return ciag
    def push(self,value):
        Node.append(self.value)





list_=LinkedList()
list_.push(1)

