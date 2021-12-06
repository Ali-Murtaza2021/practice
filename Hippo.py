from os import name
from typing import AsyncGenerator


class Animals (object):
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def description (self):
        print(self.name)
        print(self.age)

Hippo=Animals("Lion",10)
print(Hippo.description())