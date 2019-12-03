from module_masses import masses

def find_req(module):
    fuel_req = int(int(module) / 3) - 2
    return fuel_req

def find_req_with_fuel(module):
    module_req = 0
    keep_going = True
    while keep_going:
        fuel_req = int(int(module) / 3) - 2
        if fuel_req < 0:
            keep_going = False
            break
        module_req += fuel_req
        module = fuel_req
        print(module)

    return module_req


def calc_fuel_req(mass_str, problem):
    fuel_req = 0
    mass_list = mass_str.split('\n')
    for module in mass_list:
        if problem == 1:
            module_req = find_req(module)
        elif problem == 2:
            module_req = find_req_with_fuel(module)
        fuel_req += module_req

    return fuel_req