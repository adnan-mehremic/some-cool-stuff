# simple password generator


import random

population = "qwertzuiopasdfghjklyxcvbnm1234567890QWERTZUIOPASDFGHJKLYXCVBNM?0=:.,-_@!#$%&/(){}ˇ^*"

password_length = 16

your_password = "".join(random.sample(population, password_length))

print(your_password)
