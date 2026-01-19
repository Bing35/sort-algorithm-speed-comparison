#sort by na sales

import csv
import os
import pprint
import time

def main():
    csvFile = 'vgsales.csv'
    data = []
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(scriptDir, csvFile)
    
    with open(filePath, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)            
        for row in reader:
                row['NA_Sales'] = float(row['NA_Sales'])
                row['EU_Sales'] = float(row['EU_Sales'])
                row['JP_Sales'] = float(row['JP_Sales'])
                row['Other_Sales'] = float(row['Other_Sales'])
                row['Global_Sales'] = float(row['Global_Sales'])
                data.append(row)
    

    dataSet50 = data[:50]
    dataSet1000 = data[:1000]
    dataSetTotal = data


    start = time.time()
    bubbleSortSlow(dataSet50, 'NA_Sales')
    end = time.time()
    print(f"Bubble Sort slow (50): {end - start} seconds")

    start = time.time()
    bubbleSortSlow(dataSet1000, 'NA_Sales')
    end = time.time()
    print(f"Bubble Sort slow (1000): {end - start} seconds")

    start = time.time()
    bubbleSortSlow(dataSetTotal, 'NA_Sales')
    end = time.time()
    print(f"Bubble Sort slow (Total): {end - start} seconds")


#--------------------------------
    start = time.time()
    bubbleSort(dataSet50, 'NA_Sales')
    end = time.time()
    print(f"Bubble Sort (50): {end - start} seconds")

    start = time.time()
    bubbleSort(dataSet1000, 'NA_Sales')
    end = time.time()
    print(f"Bubble Sort (1000): {end - start} seconds")

    start = time.time()
    bubbleSort(dataSetTotal, 'NA_Sales')
    end = time.time()
    print(f"Bubble Sort (Total): {end - start} seconds")

# --------------------------------
    start = time.time()
    mergeSort(dataSet50.copy(), 'NA_Sales')
    end = time.time()
    print(f"Merge Sort (50): {end - start} seconds")

    start = time.time()
    mergeSort(dataSet1000.copy(), 'NA_Sales')
    end = time.time()
    print(f"Merge Sort (1000): {end - start} seconds")

    start = time.time()
    mergeSort(dataSetTotal.copy(), 'NA_Sales')
    end = time.time()
    print(f"Merge Sort (Total): {end - start} seconds")

def bubbleSortSlow(data, dictKey):
    data = data.copy()
    n = len(data)
    for tries in range(n):
        for i in range(0, n-1):
            if data[i][dictKey] > data[i + 1][dictKey]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


def bubbleSort(data, dictKey):
    data = data.copy()
    n = len(data)
    for tries in range(n):
        for i in range(0, n - tries - 1):
            if data[i][dictKey] > data[i + 1][dictKey]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data

def mergeSort(data, dictKey):
    if len(data) <= 1:
        return data

    middle = len(data) // 2
    left = mergeSort(data[:middle], dictKey)
    right = mergeSort(data[middle:], dictKey)

    result = []
    l = 0
    r = 0
    
    while l < len(left) and r < len(right):
        if left[l][dictKey] <= right[r][dictKey]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            
    result.extend(left[l:])
    result.extend(right[r:])
    return result

if __name__ == "__main__":
    main()


