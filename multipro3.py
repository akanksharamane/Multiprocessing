import os
import multiprocessing
def Add(num1,num2):
    print(os.getpid())
    print("Addition of numbers: ",num1+num2)

def Sub(num1,num2):
    print(os.getpid())
    print("Subtraction of numbers: ",num1-num2)

def main():
    p1 = multiprocessing.Process(target=Add,args=(5,3))
    p2 = multiprocessing.Process(target=Sub,args=(5,3))

    p1.start()
    p2.start()
    print("Process id : ",p1.pid)
    print("Process id : ",p2.pid)

    p1.join()
    p2.join()

if __name__=="__main__":
    print(os.getpid())
    main()