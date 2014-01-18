# Name: Laser Nite
# Kerberos: nite
# Homework_4.py


# Exercise 8.3 - Your First Class

class Queue():
    def __init__(self):
        self.line = []

    def insert(self, item):
        self.line.append(item)

    def remove(self):
        if len(self.line) > 0:
            return self.line.pop(0)
        else:
            return "The queue is empty"





