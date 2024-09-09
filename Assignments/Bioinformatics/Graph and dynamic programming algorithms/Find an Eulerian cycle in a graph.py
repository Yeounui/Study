from random import choice as ch

def file_to_dict(textfile):
    with open(textfile, 'r') as openfile:
        graphDict = {}
        for i in openfile.readlines():
            fromNode, toNode = i.strip().split(sep=' -> ')
            graphDict[fromNode] = toNode.split(sep=',')
    # {'0': ['3'], '1': ['0'], '2': ['1', '6'], ...}
    return graphDict

def connect_2(con1, con2):
    # "1-2-13", "13-22" to "1-2-13-22"
    con1, con2 = con1.split("-"), con2.split("-")
    result = con1[:-1] + con2
    return "-".join(result)

def first_of(bar_string):
    # "1-2-13" to "1"
    return bar_string.split("-")[0]

def last_of(bar_string):
    # "1-2-13" to "13"
    return bar_string.split("-")[-1]

def connect_many(as_dict):

    def remove_from_dict(bar_string):
        # remove '2-6' from {'1': ['0'], '2': ['1', '6']} ->{'1': ['0'], '2': ['1']}
        # remove '1-0' from {'1': ['0'], '2': ['1']} -> {'2': ['1']}
        left, right = bar_string.split("-")
        del as_dict[left][as_dict[left].index(right)]
        if len(as_dict[left]) == 0:
            del as_dict[left]

    start_l = ch(list(as_dict.keys()))
    start_r = ch(as_dict[start_l])
    start = f"{start_l}-{start_r}"
    remove_from_dict(start)
    cycle = start

    while last_of(cycle) in as_dict:  # still more connections possible, make init_cycle
        candidates = [f"{last_of(cycle)}-{x}" for x in as_dict[last_of(cycle)]]
        if not candidates:
            break
        selected = ch(candidates)
        remove_from_dict(selected)
        cycle = connect_2(cycle, selected)

    while as_dict:  # still more connections possible, make new_cycle
        for i in set(cycle.split("-")) & set(list(as_dict.keys())):
            # find intersection of original cycle & unconnected connections
            new_start = ch([f"{i}-{x}" for x in as_dict[i]])
            remove_from_dict(new_start)
            break
        new_cycle = new_start
        while last_of(new_cycle) in as_dict:  # same structure as init_cycle part
            candidates = [f"{last_of(new_cycle)}-{x}" for x in as_dict[last_of(new_cycle)]]
            if not candidates:
                break
            selected = ch(candidates)
            remove_from_dict(selected)
            new_cycle = connect_2(new_cycle, selected)
        cycle = "-".join(join_cycle(cycle.split("-"), new_cycle.split("-")))  # join init_cycle and new_cycle
    return cycle

def join_cycle(cycle, new_cycle):  # take lists
    if len(new_cycle) == 0:
        return cycle
    i = new_cycle[0]  # since new cycle starts from junction with init_cycle
    result = cycle[:cycle.index(i)] + new_cycle + cycle[cycle.index(i) + 1:]
    return result

def eulerian_cycle(file):
    as_dict = file_to_dict(file)  # read data,
    result = connect_many(as_dict)  # connect them in bar-string format,
    result = result.split("-")  # change to list,
    result = tuple(map(int, result))  # str to int
    return result

print(eulerian_cycle('data01.txt'))