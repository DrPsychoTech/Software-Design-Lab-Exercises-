def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  

HashTable = [[] for _ in range(10)]
  

def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  
  

def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
  
# Driver Code
insert(HashTable, 6, 'Christian')
insert(HashTable, 12, 'Kenneth')
insert(HashTable, 18, 'Flores')
insert(HashTable, 24, 'Gonzales')
insert(HashTable, 30, 'The')
insert(HashTable, 36, 'Thirdy')
  
display_hash (HashTable)