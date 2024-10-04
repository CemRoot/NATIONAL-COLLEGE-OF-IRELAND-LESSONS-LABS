
"""Exercise 5 
Write a program that will loop over the following list: a = [8, 9, 10, 11, 13, 81, 101, 100, 94]. If number is prime, print its square. Use continue keyword. """
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
# find the index of list the prime number also  print the square of the prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    ask = input("Enter the list of numbers separated by comma: ")
    a = [int(x) for x in ask.split(",")]
    for i in a:
        if is_prime(i):
            print(f"Index of prime number {i} is {a.index(i)} and its square is {i**2}")
        else:
            continue

if __name__ == "__main__":
    main()



