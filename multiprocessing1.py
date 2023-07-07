# import multiprocessing

# print("Number of core:",multiprocessing.cpu_count())
# # support more than one processor at the same time.

import os
import multiprocessing
def Square(num):
    print(os.getpid())
    print("Square of the number: ",num*num)

def Cube(num):
    print(os.getpid())
    print("Cube of the number: ",num*num*num)

def main():
    p1 = multiprocessing.Process(target=Square,args=(3,))
    p2 = multiprocessing.Process(target=Cube,args=(3,))

    p1.start()
    p2.start()
    print("Process id : ",p1.pid)
    print("Process id : ",p2.pid)

    p1.join()
    p2.join()

if __name__=="__main__":
    print(os.getpid())
    main()