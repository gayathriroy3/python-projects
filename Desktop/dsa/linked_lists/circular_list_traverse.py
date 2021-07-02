class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular:
    def __init__(self):
        self.head=None
    #def push(self,data):   #for singly linked list
     #   node=Node(data)
      #  node.next=self.head
       # self.head=node
    def push(self,data):
        node=Node(data)
        node.next=self.head
        if self.head is not None:
            tmp=self.head
            while tmp.next!=self.head :
                tmp=tmp.next
            tmp.next=node
        else:
            node.next=node
        self.head=node
    def print(self):
        tmp=self.head
        while tmp:
            print(tmp.data)
            tmp=tmp.next
            if tmp==self.head:
                break
if __name__=="__main__":
    clist=Circular()
    clist.push(8)
    clist.push(7)
    clist.push(5)
    clist.push(2)
    clist.print()


