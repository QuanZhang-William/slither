
from .variable import SlithIRVariable
from slither.core.variables.local_variable import LocalVariable
from slither.core.children.child_node import ChildNode

class LocalIRVariable(LocalVariable, SlithIRVariable):

    def __init__(self, local_variable):
        assert isinstance(local_variable, LocalVariable)

        super(LocalIRVariable, self).__init__()

        # initiate ChildContract
        self.set_function(local_variable.function)

        # initiate Variable
        self._name = local_variable.name
        self._initial_expression = local_variable.expression
        self._type = local_variable.type
        self._initialized = local_variable.initialized
        self._visibility = local_variable.visibility
        self._is_constant = local_variable.is_constant

        # initiate LocalVariable
        self._location = self.location

        self._index = 0

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, idx):
        self._index = idx

    @property
    def ssa_name(self):
        return '{}_{}'.format(self._name, self.index)