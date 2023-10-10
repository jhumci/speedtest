def sort_1(arr):
    """bubble_sort"""
    n = len(arr)
        
    for i in range(n):
        # Letzte i Elemente sind bereits sortiert
        for j in range(0, n-i-1):
            # Durchlaufe das Array von 0 bis n-i-1
            # Swap, wenn das Element größer ist als das nächste
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

#print(sort_1([12,3,4,5]))