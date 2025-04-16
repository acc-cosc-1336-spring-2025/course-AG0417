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

def get_p_distance(list1, list2):
    mismatches = 0
    for a, b in zip(list1, list2):
        if a != b:
            mismatches += 1
    return mismatches / len(list1)

def get_p_distance_matrix(lists):
    n = len(lists)
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            distance = get_p_distance(lists[i], lists[j])
            row.append(distance)
        matrix.append(row)
    return matrix