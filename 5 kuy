def pick_peaks(arr):
    """
    function that returns the positions and the values of the "peaks"
    (or local maxima) of a numeric array.
    """
    answer = {"pos": [], "peaks": []}
    pos, peak = 0, 0
    for i in range(1, len(arr)):
        if arr[i]>arr[i-1]:
            pos, peak = i, arr[i]
        elif arr[i]<arr[i-1]:
            answer["pos"] += pos
            answer["peaks"] += peak
            pos, peak = 0, 0
    return answer
