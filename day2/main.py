import numpy as np
import time
def puzzel1():
    validPasswords = 0

    data = np.loadtxt("./day2/input.txt", delimiter=": ", dtype="str")

    for [rule, password] in data:
        [bounds, letter] = rule.split(" ")
        [l_bound, u_bound] = map(int, bounds.split("-"))
        validPasswords += l_bound <= password.count(letter) <= u_bound

    print("Puzzle 1: The number of correct passwords in the dataset are: "f"{validPasswords}")

def puzzel2():

    data = np.loadtxt("./day2/input.txt", delimiter=": ", dtype="str")


    correct_passwords = 0
    for [rule, password] in data:
        [indices, letter] = rule.split(" ")
        [l_index, u_index] = map(int, indices.split("-"))
        correct_passwords += (password[l_index - 1] == letter) ^ (password[u_index - 1] == letter)

    print("Puzzle 2: The number of correct passwords in the dataset are: "f"{correct_passwords}")



if __name__ == '__main__':
    t = time.process_time()
    puzzel1()
    puzzel2()
    elapsed_time = time.process_time() - t
    print("benchpress69: ",elapsed_time*1000, "milisex")

