# In Python, dividing by zero causes an exception, so you should
# return None instead.
#
# Your job is to create 4 new classes which inherit the 'Operation' class.
# Within the class, create the proper execute method and save the
# mathematical operation to the proper result variable. The class
# names must be as follows:
#
# Add
# Subtract
# Multiply
# Divide

class Operation(ABC):
    def __init__(self):
        self.result = None

    @abstractmethod
    def execute(self, v1, v2):
        pass

class Add(Operation):
    def execute(self, v1, v2):
        self.result = v1 + v2

class Subtract(Operation):
    def execute(self, v1, v2):
        self.result = v1 - v2

class Multiply(Operation):
    def execute(self, v1, v2):
        self.result = v1 * v2

class Divide(Operation):
    def execute(self, v1, v2):
        try:
            self.result = v1 / v2
        except ZeroDivisionError:
            self.result = None
