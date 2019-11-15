def find_peaks(list_of_intensities):
    """Find peaks
    Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.
    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values
    Returns:
        list of floats: list of the position of identified local maxima
    Note:
        This is just a place holder for the TDD part :)
    """
    max_value = 0
    list_of_pos=list()
    for pos, element in enumerate(list_of_intensities):
        if pos == 0:
            continue
        if pos == len(list_of_intensities) - 1:
            continue
        if list_of_intensities[pos - 1] < element > list_of_intensities[pos + 1]:
            list_of_pos.append(pos)
            
    return list_of_pos
