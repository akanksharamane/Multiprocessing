import os
def Square(num):
    print(os.getpid())
    print("Square of the number: ",num*num)

def Cube(num):
    print(os.getpid())
    print("Cube of the number: ",num*num*num)

def main():
    Square(4)
    Cube(4)

if __name__=="__main__":
    print(os.getpid())
    main()