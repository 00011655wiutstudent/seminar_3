#task 1
#here name and surname are parementers
def example_1(x,y):
    print(f"Your full name is {x} {y}")
example_1("Madina", "Tolibjonva")

#here function takes name and surname as argument


#task 2
def example_1(name, surname):
    print("Your full name is {} {}".format(name, surname))


name = input("What is your name ? ")
surname = input("What is your surname ? ")
def example_2(name, surname):
    print("Your full name is {} {}".format(name, surname))


name = input("What is your name ? ")
surname = input("What is your surname ? ")

def example_3(a):
    print(f"Your full mark is {a}")

example_3(46+79)

#task 3
def task_3():
    my_name = "Madina"
    print(f"My name is {my_name}")


task_3()
#print(my_name) won't work as the my name is local variable

#task 4
def task_4(age):
    print(f"Your pet's age is {age}")

task_4(78)
#print(age) won't work as the paramentr works only within the function and saves variable local.

#task 5
#We have variable task_5_name and if I change it locally it will change only for this function and global
#variable will stay the same
task_5_name = "00011655"
def task_5():
    task_5_name = "Dilnova"
    print(f"My name is {task_5_name}")

task_5()
print(task_5_name)
