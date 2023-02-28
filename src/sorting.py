def partition(vectors, low, high, keyIdx):
    pivot = vectors[high][keyIdx]
    i = low - 1

    for j in range(low, high):
        if vectors[j][keyIdx] <= pivot:
            i = i + 1
            (vectors[i], vectors[j]) = (
                vectors[j],
                vectors[i],
            )

    (vectors[i + 1], vectors[high]) = (
        vectors[high],
        vectors[i + 1],
    )
    return i + 1


def quicksort(vectors, low, high, keyIdx=0):
    if low < high:
        pi = partition(vectors, low, high, keyIdx)

        quicksort(vectors, low, pi - 1, keyIdx)
        quicksort(vectors, pi + 1, high, keyIdx)
