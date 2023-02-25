import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


N = 128


def merge(A, p, q, r):
    """Merge two sorted sublists/subarrays to a larger sorted sublist/subarray.
    Arguments:
    A -- a list/array containing the sublists/subarrays to be merged
    p -- index of the beginning of the first sublist/subarray
    q -- index of the end of the first sublist/subarray;
    the second sublist/subarray starts at index q+1
    r -- index of the end of the second sublist/subarray
    """
    # start_time_merge = time.time()
    # Copy the left and right sublists/subarrays.
    # If A is a list, slicing creates a copy.
    if type(A) is list:
        left = A[p: q + 1]
        right = A[q + 1: r + 1]
    # Otherwise a is a np.array, so create a copy with list().
    else:
        left = list(A[p: q + 1])
        right = list(A[q + 1: r + 1])

    i = 0  # index into left sublist/subarray
    j = 0  # index into right sublist/subarray
    k = p  # index into a[p: r+1]

    # Combine the two sorted sublists/subarrays by inserting into A
    # the lesser exposed element of the two sublists/subarrays.

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    # After going through the left or right sublist/subarray, copy the
    # remainder of the other to the end of the list/array.
    if i < len(left):  # copy remainder of left
        A[k: r + 1] = left[i:]
    if j < len(right):  # copy remainder of right
        A[k: r + 1] = right[j:]

    # end_time_merge = time.time()
    # print("Execution Merge Time: --- %s seconds ---" % (end_time_merge - start_time_merge))


def merge_sort(A, use_insertion_sort=False, p=0, r=None):
    """Sort the elements in the sublist/subarray a[p:r+1].
    Arguments:
    A -- a list/array containing the sublist/subarray to be merged
    p -- index of the beginning of the sublist/subarray (default = 0)
    r -- index of the end of the sublist/subarray (default = None)
    """

    # If r is not given, set to the index of the last element of the list/array.
    if r is None:
        r = len(A) - 1
    if p >= r:  # 0 or 1 element?
        return

    portion = (r - p) + 1

    if use_insertion_sort and portion < N:
        # print('Smaller : ' + str(r - p))
        insertion_sort(A, p, portion)
        return

    q = (p + r) // 2  # midpoint of A[p: r]
    merge_sort(A, use_insertion_sort, p, q)  # recursively sort A[p: q]
    merge_sort(A, use_insertion_sort, q + 1, r)  # recursively sort A[q+1: r]
    merge(A, p, q, r)  # merge A[p: q] and A[q+1: r] into A[p: r]


def merge_sort_helper(A, use_insertion_sort=False, p=0, r=None):
    start_time_sort = datetime.now()
    merge_sort(A, use_insertion_sort)
    end_time_sort = datetime.now()
    diff = end_time_sort - start_time_sort
    return diff
    #print("Execution Sort Time: --- %s seconds ---" % (
    #    end_time_sort - start_time_sort))  # input should be bigger to avoid error of time mesurement


def insertion_sort(A, start, n):
    """Sort a list or numpy array.
    Argument:
    A -- a list or numpy array
    start -- start index in A
    n -- portion size in A
    """
    # Traverse the list or array from index 1 to n-1.
    # print("Insert : start : " + str(start) + " portion : "+ str(n))
    for i in range(1, n):
        key = A[start + i]

        # Insert A[i] into the sorted subarray a[0:i].
        # Compare stored key with the already sorted values to its left.
        # Move each item one position to the right until we find the
        # position for the key or fall off the left end of the list or array.
        j = i - 1
        while j >= 0 and A[start + j] > key:
            A[start + j + 1] = A[start + j]
            j -= 1

        # Insert key at the correct position in the list or array.
        A[start + j + 1] = key


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Testing with different input:
    listInputs = [10000, 20000, 40000, 80000, 100000, 160000, 320000]
    listTimesV = [None] * len(listInputs)
    listTimesM = [None] * len(listInputs)
    for i in range(0,len(listInputs)):
        input = np.random.randint(-5000, 5000, size=listInputs[i])
        print("Input Size : " + str(input.size) + " N : " + str(N))
        list1 = np.copy(input)
        list1test = list(list1)
        print("vanilla MergeSort")
        timeDiff_V = merge_sort_helper(list1).total_seconds() * 10**3
        print(f"Execution time for just merge sort for input size of {listInputs[i]}: {timeDiff_V:.03f}ms")
        listTimesV[i] = timeDiff_V
    
        list2 = np.copy(input)
        list2test = list(list2)
        print("MergeSort + InsertionSort for N : " + str(N))
        timeDiff_M = merge_sort_helper(list2, use_insertion_sort=True).total_seconds() * 10**3
        print(f"Execution time for merge + insertion sort for input size of {listInputs[i]}: {timeDiff_M:.03f}ms")
        listTimesM[i] = timeDiff_M
    
    #ploting the graph
    # X axis parameter:
    xaxis = listInputs
    # Y axis parameter:
    yaxis = listTimesV
    # X axis parameter:
    xaxis2 = listInputs
    # Y axis parameter:
    yaxis2 = listTimesM
    # graph details:
    plt.xlabel("InputSize")
    plt.ylabel("TimeTaken ms")
    plt.title("InputSize vs ExecutionTime")
    plt.plot(xaxis, yaxis, linestyle='--', marker='.', color='b', label='')
    plt.grid(color='c', linestyle='-', linewidth=1)

    plt.plot(xaxis, yaxis2, linestyle='--', marker='.', color='g', label='')
    plt.grid(color='c', linestyle='-', linewidth=1)
    for i in range(0,len(listInputs)):
        plt.annotate(f"{listTimesV[i]:.03f}ms ", (listInputs[i] - 500, listTimesV[i]+ 25))
        plt.annotate(f"{listTimesM[i]:.03f}ms ", (listInputs[i], listTimesM[i]- 50))
    plt.show()

