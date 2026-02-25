numbers = input("Enter numbers separated by space: ").split()
num_list = [int(n) for n in numbers]   
num_tuple = tuple(num_list)            
print("List:", num_list)
print("Tuple:", num_tuple)
for num in num_list:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
