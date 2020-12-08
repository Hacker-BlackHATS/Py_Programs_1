from time import time
from random import randint


def menu():
    print("Choose any one of the following options ::")
    print("1.> 1 Question\n2.> 5 Question Series\n3.> 10 Question Series\n4.> Exit")
    opt = input(">>>  ")
    if opt == "1":
        return 1
    elif opt == "2":
        return 5
    elif opt == "3":
        return 10
    elif opt == "4":
        print("Thank you for playing!!!\nSEE YOU SOON......")
        exit(0)
    else:
        print("Please enter a valid option!!!")
        menu()


def table_start(n):
    result_dict = {"correct": 0, "incorrect": 0, "total_time": 0.00, "average_time": 0.00}
    for i in range(n):
        a = randint(2, 9)
        b = randint(1, 11)
        start_time = time()
        ans1 = int(input(f"{a} X {b} = "))
        finish_time = time() - start_time
        result_dict["total_time"] += finish_time
        if a * b == ans1:
            result_dict["correct"] += 1
        else:
            result_dict["incorrect"] += 1
    if n > 1:
        result_dict["average_time"] = result_dict["total_time"]/n
    elif n == 1:
        result_dict["average_time"] = result_dict["total_time"]
    return result_dict


def results(r):
    print("Your result ::")
    print(f'Correct answers = {r["correct"]}')
    print(f'Incorrect answers = {r["incorrect"]}')
    print(f'Total Time Taken = {r["total_time"]} seconds')
    print(f'Average Time Taken = {r["average_time"]} seconds')


def table_tester():
    result = table_start(menu())
    results(result)


if __name__ == "__main__":
    table_tester()
