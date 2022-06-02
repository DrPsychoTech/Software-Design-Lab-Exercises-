# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #delete all nodes of the list
  def deleteAllNodes(self):
    while (self.head != None):
      temp = self.head
      self.head = self.head.next
      temp = None
    print("All nodes are deleted successfully.")

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code
MyList = LinkedList()

#Add four elements in the list.
MyList.push_back(5)
MyList.push_back(10)
MyList.push_back(15)
MyList.push_back(20)

#Display the content of the list.
MyList.PrintList()

#delete all nodes of the list
MyList.deleteAllNodes()

#Display the content of the list.
MyList.PrintList()
