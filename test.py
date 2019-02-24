from slither.slither import Slither
import itertools
from priority import WAWNode
from priority import RAWNode
import datetime

t1 = datetime.datetime.now()

slither = Slither('depth_hack/internal_call.sol')
slither_contract = slither.get_contract_from_name('Caller')

functions = slither_contract.functions

depdency_dict = {}

for func in slither_contract.functions:
    if func.full_name not in slither_contract.disassembly.slither_mappings_dict.keys():
        continue

    # for outer dictionary
    depdency_dict[func.full_name] = {}
    outer_var_temp = func.state_variables_written_including_internal_calls
    outer_func_temp = set()

    for write_var in outer_var_temp:
        outer_func_temp = outer_func_temp.union(slither_contract.get_functions_reading_from_variable_including_internal_call(write_var))

    for reading_func in outer_func_temp:
        var_temp = set()
        func_temp = set()

        for var_read in reading_func.state_variables_read_including_internal_calls:
            var_temp.add(var_read)

        for var_read in var_temp:
            func_temp = func_temp.union(slither_contract.get_functions_writing_to_variable_including_internal_call(var_read))

        # for inner dictionary
        depdency_dict[func.full_name][reading_func.full_name] = func_temp


print('i love you')

#print(a)
#s_v = contract.state_variables
#var_a = contract.get_state_variable_from_name('aa')
#functions_reading = contract.get_functions_reading_from_variable(var_a)
#functions_writing_a = contract.get_functions_writing_to_variable_including_internal_call(var_a)
#functions_reading_a = contract.get_functions_reading_from_variable_including_internal_call(var_a)


#for func in functions_writing_a:
#    testt = func.func_signature_mythril_compact()
#testa = contract.all_functions_called()



# Print the result
#print('The function reading "a" are {}'.format([f.name for f in functions_reading_a]))
#print('The function writing "a" are {}'.format([f.name for f in functions_writing_a]))


