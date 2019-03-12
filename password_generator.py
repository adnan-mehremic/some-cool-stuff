# simple password generator
import random

population = "qwertzuiopasdfghjklyxcvbnm1234567890QWERTZUIOPASDFGHJKLYXCVBNM?0=:.,-_@!#$%&/(){}ˇ^*"

password_length = input("Please put length of password: ")

your_password = "".join(random.sample(population, int(password_length)))

print("Your password is:", your_password)
