"""
Hekay Programming Language

Memory Manager

Developer: Dhiraj Kumar Mehangiya
"""


class Memory:

    def __init__(self):
        self.variables = {}
        self.constants = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name)

    def set_constant(self, name, value):
        self.constants[name] = value

    def get_constant(self, name):
        return self.constants.get(name)

    def show(self):
        print("=== Variables ===")
        for name, value in self.variables.items():
            print(f"{name} = {value}")

        print("\n=== Constants ===")
        for name, value in self.constants.items():
            print(f"{name} = {value}")