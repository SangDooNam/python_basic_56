# TODO implement bubble sort

def bubblesort(in_list: list) -> list:
    swaps = False
    for i in range(len(in_list) -1 ):
        if in_list[i] > in_list[i+1]:
            in_list[i], in_list[i+1] = in_list[i+1], in_list[i]
            swaps = True
    if swaps:
        bubblesort(in_list)
    return in_list
