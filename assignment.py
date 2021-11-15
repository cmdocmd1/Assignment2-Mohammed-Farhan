import csv
import array as arr
import pandas as pd

array1 = arr.array("i")
tuple1 = ()
list1 = []
set1 = set()
dictionary1 = dict()

rows = []

def print_type(): #printing the type of the variables
    print(type(array1))
    print(type(tuple1))
    print(type(list1))
    print(type(set1))
    print(type(dictionary1))

def write_result(): #write results in assignment2_file.txt in opposite order
    opposite = rows[::-1] 
    with open("assignment2_file.txt", "w") as file:
        for i in range(len(opposite)):
            file.write(str(opposite[i]) + "\n")

def print_result(): #priting the result of the assignment2_file.txt
    with open('assignment2_file.txt') as f:
        lines = f.readlines()
        for i in range (len(lines)):
            print(lines[i])

def insert_value(): #adding variables inside the array1, tuple1, list1, set1 and dictionary1 
    with open('assignment2_file.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)

    for i in range(len(rows[0])):
        array1.append(int(rows[0][i]))

    for i in range(len(rows[2])):
        list1.append(rows[2][i])
    
    for i in range(len(rows[3])):
        set1.add(rows[3][i])
    
    for i in range(len(rows[4])):#  key:value
        dictionary1.update({rows[4][i] : rows[5][i]})

def append_result(): #add more text to assignment2_file.txt
    with open("assignment2_file.txt","a") as file:
        for i in range(len(array1)):
            file.write(str(array1[i]) + "\n")
        for i in range(len(list1)):
            file.write(str(list1[i]) + "\n")
        file.write(str(set1))
        for t in tuple1:
            line = ' '.join(str(x) for x in t)
            file.write(line + '\n')

def search_value(): #searching for values

    for i in range(len(list1)):
        if list1[i] == "Fujairah":
            print(str(list1[i]) + "\n")

    if "brown" in set1:
            print("brown")
    
    for i, j in dictionary1.items():  
        if j == "Data Science":
            print(i)

def sort_dictionary():
    for i in sorted (dictionary1) :
        print ((i, dictionary1[i]), end =" ")

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def merge(A):
    if len(A) > 1:
        evens = []
        odds = []
        for i in range(len(A)):
            if i % 2 == 0:
                evens.append(A[i])
            else:
                odds.append(A[i])
                
        print(evens, odds)
        #spliting again
        merge(evens)
        merge(odds)

        i = j = k = 0
        #R- odd  L- even
        while i < len(evens) and j < len(odds):
            if evens[i] < odds[j]:
                A[k] = evens[i]
                i += 1
            else:
                A[k] = odds[j]
                j += 1
            k += 1

        while i < len(evens):
            A[k] = evens[i]
            i += 1
            k += 1
  
        while j < len(odds):
            A[k] = odds[j]
            j += 1
            k += 1

def new_vsc():
    read_file = pd.read_csv ("assignment2_file.txt")
    read_file.to_csv ("assignment22_file.csv", index=None)

def main():
    insert_value()
    write_result()
    print_result()
    search_value()
    insertionSort(array1)
    merge(tuple1)
    quickSort(list1, 0, len(list1)-1)
    #quickSort(set1, 0, len(set1)-1)
    sort_dictionary()
    append_result()
    new_vsc()




main()