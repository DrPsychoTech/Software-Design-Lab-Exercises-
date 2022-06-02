class Node:
    def __init__(self):
        self.coeff = None
        self.power = None
        self.next = None


# Function add a new node at the end of list
def addnode(start, coeff, power):
    # Create a new node
    newnode = Node();
    newnode.coeff = coeff;
    newnode.power = power;
    newnode.next = None;

    # If linked list is empty
    if (start == None):
        return newnode;

    # If linked list has nodes
    ptr = start;
    while (ptr.next != None):
        ptr = ptr.next;
    ptr.next = newnode;
    return start;


# Function To Display The Linked list
def printList(ptr):
    while (ptr.next != None):
        print(str(ptr.coeff) + 'x^' + str(ptr.power), end='')
        if (ptr.next != None and ptr.next.coeff >= 0):
            print('+', end='')
        ptr = ptr.next
    print(ptr.coeff)


# Function to add coefficients of
# two elements having same powerer
def removeDuplicates(start):
    ptr2 = None
    dup = None
    ptr1 = start;

    # Pick elements one by one
    while (ptr1 != None and ptr1.next != None):
        ptr2 = ptr1;

        # Compare the picked element
        # with rest of the elements
        while (ptr2.next != None):

            # If powerer of two elements are same
            if (ptr1.power == ptr2.next.power):

                # Add their coefficients and put it in 1st element
                ptr1.coeff = ptr1.coeff + ptr2.next.coeff;
                dup = ptr2.next;
                ptr2.next = ptr2.next.next;

            else:
                ptr2 = ptr2.next;

        ptr1 = ptr1.next;


# Function two Multiply two polynomial Numbers
def multiply(poly1, Npoly2, poly3):
    # Create two pointer and store the
    # address of 1st and 2nd polynomials
    ptr1 = poly1;
    ptr2 = poly2;

    while (ptr1 != None):
        while (ptr2 != None):
            # Multiply the coefficient of both
            # polynomials and store it in coeff
            coeff = ptr1.coeff * ptr2.coeff;

            # Add the powerer of both polynomials
            # and store it in power
            power = ptr1.power + ptr2.power;

            # Invoke addnode function to create
            # a newnode by passing three parameters
            poly3 = addnode(poly3, coeff, power);

            # move the pointer of 2nd polynomial
            # two get its next term
            ptr2 = ptr2.next;

        # Move the 2nd pointer to the
        # starting point of 2nd polynomial
        ptr2 = poly2;

        # move the pointer of 1st polynomial
        ptr1 = ptr1.next;

    # this function will be invoke to add
    # the coefficient of the elements
    # having same powerer from the resultant linked list
    removeDuplicates(poly3);
    return poly3;


# Driver Code
if __name__ == '__main__':
    poly1 = None
    poly2 = None
    poly3 = None;

    # Creation of 1st Polynomial: 3x^2 + 5x^1 + 6
    poly1 = addnode(poly1, 3, 3);
    poly1 = addnode(poly1, 6, 1);
    poly1 = addnode(poly1, -9, 0);

    # Creation of 2nd polynomial: 6x^1 + 8
    poly2 = addnode(poly2, 9, 3);
    poly2 = addnode(poly2, -8, 2);
    poly2 = addnode(poly2, 7, 1);
    poly2 = addnode(poly2, 2, 0);

    # Displaying 1st polynomial
    print("1st Polynomial:- ", end='');
    printList(poly1);

    # Displaying 2nd polynomial
    print("2nd Polynomial:- ", end='');
    printList(poly2);

    # calling multiply function
    poly3 = multiply(poly1, poly2, poly3);

    # Displaying Resultant Polynomial
    print("Resultant Polynomial:- ", end='');
    printList(poly3);