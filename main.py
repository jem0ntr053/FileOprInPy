# a1p1 takes the name of a file as input,
# accesses the file, and prints the files title to the output.
def a1p1():
    print("Problem 1:")
    fname = input("Enter your file name: \n")
    with open(fname, 'w', encoding='utf-8') as f:
        print('Name of the file: ', f.name + "\n")


# a1p2 is a program that takes user input and implements file operations to
# read, write, and organize data from files.
def a1p2():
    print("Problem 2:")

    # Have the user input names, then reverse the names and save to file1.txt
    with open('file1.txt', 'w+') as f1:
        names = list(map(str, input('Enter student names separated with spaces:'
                                    '\n').split()))
        rev_str = [i[::-1] for i in names]
        for item in rev_str:
            f1.write("%s\n" % item)

    # Read names from file1 and reverse them (to normal) and save to file2.txt
    with open('file1.txt', 'r') as f:
        names = f.read().split()
        with open('file2.txt', 'w') as f2:
            rev_str = [i[::-1] for i in names]
            for item in rev_str:
                f2.write("%s\n" % item)

    # Read names from file2 and reverse them again,
    #  then print them to the screen.
    with open('file2.txt', 'r') as f:
        names = f.read().split()
        rev_str = [i[::-1] for i in names]
        rev_str.sort()
        for item in rev_str:
            print("%s" % item)

    # f2 = open("file2.txt", "r")
    # file2 = f2.read().split()
    # for i in file2:
    #     file2 = [i[::-1]]
    #     file2.sort()
    #     for item in file2:
    #         print(item)
    #
    # f2.close()


if __name__ == '__main__':
    a1p1()
    a1p2()
