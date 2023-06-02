def remove_duplicates(lst):
    unique_dict = {}
    result = []
    for item in lst:
        if tuple(item.items()) not in unique_dict:
            unique_dict[tuple(item.items())] = True
            result.append(item)
    return result