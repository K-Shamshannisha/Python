# Python dsa ->ARRAY
from array import *
array1=array('i',[10,20,30,40,50]) #creation
for x in array1:
    print(x) #print
print(array1[3]) #access
print(array1[1:4])

array1.insert(1,90) #insertion
for x in array1:
    print(x) 

array1.remove(50) #deletion
for x in array1:
    print(x) 

print(array1.index(10)) #search index of element

array1[3]=240
for x in array1:
    print(x) #update

# 
# Python dsa ->LISTS
list1=[20,'sham',2002,'d',20.9] #creation
print (list1)

print(list1[1]) #access
print(list1[2:4])

list1[1]="athiq" #updation
print(list1)

del list1[2] #deletion
print(list1)

#
# Python dsa ->TUPLE
tuple1=("sham",'q',2002,40.6,309) #creation
print(tuple1)

print(tuple1[4]) #access
print(tuple1[0:5])

#tuple1[3]=888 #gives ERROR 
# print(tuple1) #gives ERROR
tuple2=(888,"k") #update
tuple1=tuple1+tuple2
print(tuple1)

# del tuple1[0] #ERROR
del tuple1
# print(tuple1) #DELETION OFF TUPLE

#
# Python dsa ->DICTIONARY
dict1={'Name':"sham","age":24,"class":'j',"kan":487.96} #creation
print(dict1)

print(dict1["age"]) #access by keys

dict1["Name"]="afsha" #update
print(dict1)

del dict1["kan"] #deletion
print(dict1)

#
# Python dsa ->SETS
sett=set(["kan","van",986,56.0]) #creation
print(sett)

# print(set1[3]) ERROR
for i in sett: #access all
    print(i)

sett.add('h') #update
print(sett)

sett.remove('h') 
sett.discard(56.0)#deletion
print(sett)

# Union of SET
set1=set(["sham",'d',2002,40.6,309])
set2=set(["sun","ran",98.54,543,'d'])
uni=set1|set2
print(uni)

#Insertion of SET
inse=set1&set2
print(inse)

# Difference of SET
dif=set1-set2
print(dif)

# Compare SETS
Subsets=set1<=set2
Superset=set1>=set2
print(Subsets)
print(Superset)

#
# Python DSA->MAPS
#CREATING A CHAINMAP
import collections
dict2={'day1':'Mon','day2':'tues','day3':'wed'}
dict3={'day4':'thus','day5':'fri','day6':'sat'}
res=collections.ChainMap(dict2,dict3)
# creating single dictionary
print(res.maps,'\n')

#accessing keys and values
print('keys={}'.format(list(res.keys())))
print('values={}'.format(list(res.values())))
print()

#print all elements from res
print('elements:')
for keys,val in res.items():
    print('{}={}'.format(keys,val))
print()

#find specific value in res
print('day3 in res:{}'.format(('day1' in res)))
print('day4 in res:{}'.format(('day4' in res)))

#MAP REORDERING
res=collections.ChainMap(dict3,dict2)
print(res.maps,'\n')

#UPDATING MAP
dict2['day7']='sun'
print(res.maps,'\n')

# 
# Python DSA->LINKED LISTS
#Creation of LINKEDLIST
class Node: #Create a NODE
    def __init__(self,data=None):
        self.data=data
        self.next=None
node1=Node(3)
print(node1.data)
class LinkedList: #Create a LINKEDLIST
    def __init__(self):
        self.head=None
        self.last_node=None
l1=LinkedList()

# /////All methods of LINKED LIST////////
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of LL

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list
        # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list

    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data")
llist.printLL()

# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)


# print the linked list again
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())


        