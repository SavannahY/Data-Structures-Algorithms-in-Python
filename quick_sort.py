"""Implement quick sort in Python.
Input a list.
Output a sorted list"""
def quicksort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array.pop()
        greater, lesser = [],[]
        for element in array:
            if element>pivot:
                greater.append(element)
            else:
                lesser.append(element)
        return quicksort(lesser)+[pivot]+quicksort(greater)
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
