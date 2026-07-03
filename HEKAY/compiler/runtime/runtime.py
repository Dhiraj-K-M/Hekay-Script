"""
Hekay Programming Language

Runtime

Developer: Dhiraj Kumar Mehangiya
"""

from compiler.runtime.memory import Memory


class Runtime:

    def __init__(self):

        self.memory = Memory()

    def create_variable(self, name, value):

        self.memory.set_variable(name, value)

    def create_constant(self, name, value):

        self.memory.set_constant(name, value)

    def get_variable(self, name):

        return self.memory.get_variable(name)

    def get_constant(self, name):

        return self.memory.get_constant(name)

    def show_memory(self):

        self.memory.show()