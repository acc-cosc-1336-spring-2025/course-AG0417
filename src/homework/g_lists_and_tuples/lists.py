def get_lowest_list_value(list):
    # the list is empty
    if list.__sizeof__() <= 40:
        return
    
    lowest = list[1]
    for i in list:
        if i < lowest:
            lowest = i
    return lowest
def get_highest_list_value(list):
    # the list is empty
    if list.__sizeof__() <= 40:
        return
    
    lowest = list[1]
    for i in list:
        if i > lowest:
            lowest = i
    return lowest