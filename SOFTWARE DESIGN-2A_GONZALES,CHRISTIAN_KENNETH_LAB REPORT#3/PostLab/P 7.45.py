def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def main():
    list = input(" please enter a list of numbers: ")
    print("the largest number is: ", Max(list))

main()