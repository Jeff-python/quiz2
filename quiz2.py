# Quiz: FizzBuzzer class
# Part 1
# Create a class called FizzBuzzer

# It has an init method and a next val. The init method has an argument, start whose default value is 0. An integer instance property called number is set to equal start

# It has a (normal, not class) method called next that takes no arguments.

# This method increases number by 1 and then returns a string of that number's fizzbuzz value.

# Fizzbuzz value of n = "fizz" if n is evenly divisible by 3, "buzz" if n is evenly divisible by 5, and "fizzbuzz" if n is evenly divisible by 3 and 5. If n is not divisible by 3 or 5 then the fizzbuzz value is the value of n converted into a string.

# Example

# buzzer = FizzBuzzer(11)
# print(buzzer.next())
# print(buzzer.next())
# print(buzzer.next())
# print(buzzer.next())
# print(buzzer.next())
# outputs

# fizz
# 13
# 14
# fizzbuzz
# 16
# and

# buzzer = FizzBuzzer()
# print(buzzer.next())
# print(buzzer.next())
# print(buzzer.next())
# produces

# 1
# 2
# fizz




class FizzBuzzer:

    def __init__(self, i, n, lst):
        self.i = 0 #starting default value
        self.n = n #ending value
        self.lst = []
        


    def __append__(self, val):  
        for i in range(self.i,self.n):
            if val % 3 == 0 and val % 5 == 0:
                self.lst.append("fizzbuzz")
            elif val % 3 == 0:
                self.lst.append("fizz")
            elif val % 5 == 0:
                self.lst.append("buzz")
            else:
                self.lst.append(i)       

    def __next__(self):
        ret_val = self.lst[self.n]
        self.n += 1
        return ret_val

      