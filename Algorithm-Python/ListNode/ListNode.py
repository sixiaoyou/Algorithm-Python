class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class ListNode(object):
    def __init__(self):
        self.head=0

    def __getitem__(self, key):
        if self.is_empty():
            print "ListNode is empty"
            return
        elif key < 0 or key > self.getlength():
            print "The given key is error"
            return
        else:
            return self.getitem(key)

    def getLength(self):
        p = self.head
        length = 0
        while p !=0:
            length+=1
            p=p.next
        return length


    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def getitem(self,index):
        if(self.is_empty()):
            print 'ListNode is empty.'
            return
        j=0
        p=self.head
        while p.next!=0 and j<index:
            p=p.next
            j+=1
        if j==index:
            return p.data
        else:
            print 'target is not exist!'


    def append(self,item):
        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next=q
