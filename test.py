from slither.slither import Slither

slither = Slither('solidity_examples/twoStepKill.sol')
contract = slither.get_contract_from_name('Suicide')
var_a = contract.get_state_variable_from_name('owner')
functions_reading = contract.get_functions_reading_from_variable(var_a)
functions_writing_a = contract.get_functions_writing_to_variable_including_internal_call(var_a)
#testa = contract.all_functions_called()


# Print the result
print('The function reading "a" are {}'.format([f.name for f in functions_reading]))
print('The function writing "a" are {}'.format([f.name for f in functions_writing_a]))