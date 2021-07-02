class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def delete(self):
        tmp=self.head
        
        while tmp:
            prev=tmp.next
            del tmp.data
            tmp=prev
    def printlist(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next



   
   
if __name__=='__main__':
    llist=Linkedlist()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.head.next=second
    second.next=third
    llist.printlist()
    llist.delete()