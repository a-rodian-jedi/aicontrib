class InvalidCondition(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidAction(Exception):
    def __init__(self, message):
        super().__init__(message)

class ActionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidNode(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidInverter(Exception):
    def __init__(self, message):
        super().__init__(message)

class TreeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class AdjacencyListError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NodeError(Exception):
    def __init__(self, message):
        super().__init__(message)