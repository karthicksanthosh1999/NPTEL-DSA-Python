# CREATE THE NODE
class Node:
    def __init__(self,dataVal=None):
        self.dataVal = dataVal
        self.nextVal = None

#CREATE THE LINKEDLIST
class LinkedList:
    def __init__(self):
        self.headVal = None

    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.nextVal = self.headVal
        self.headVal = new_node

    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.headVal is Node:
            self.headVal = new_node
            return
        last = self.headVal
        while last.nextVal:
            last = last.nextVal
        last.nextVal = new_node

# CREATE THE OBJECT
list1 = LinkedList()

# CREATE THE NODES
list1.headVal = Node("Monday")
node2 = Node("Tursday")
node3 = Node("Wednesday")

# ASSIGN THE NODE VALUES
list1.headVal.nextVal = node2
node2.nextVal = node3
list1.insert_at_beginning("Sunday")
list1.insert_at_end("Saturday")

# PRINT THE ALL LINKEDLIST
current = list1.headVal
while current:
    print(current.dataVal)
    current = current.nextVal
