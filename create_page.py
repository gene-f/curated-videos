def group_by_type(*args):
    groups = {}
    for arg in args:
        if type(arg) not in groups.keys():
            groups[type(arg)] = [arg]
        else:
            groups[type(arg)].append(arg)
    return groups
