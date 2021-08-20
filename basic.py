# a, b, c = 3, 5, 7
# msg = a - b // c
# print(msg)
# 5.11

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t4 = [32, 5, 12, 8, 3, 75, 2, 15]

# print(max(t4))

def match2Arr(arr1,arr2):
    t3 = []
    index = 0
    while index<len(arr2) :
        t3.append(arr1[index])
        t3.append(arr2[index])
        index = index + 1
    print(t3)

def getArrValue(arr) :
    i = 0
    result = ""
    while i<len(arr):
        result = result + " " + arr[i]
        i = i + 1
    print(result)

def sortEvenOdd(arr):
    i = 0
    evenArr, oddArr = [], []
    while i < len(arr):
        if arr[i]%2 == 0 :
            evenArr.append(arr[i])
        else:
            oddArr.append(arr[i])
        i += 1
    print("Even array: " + str(evenArr) + " and odd : " + str(oddArr))


sortEvenOdd(t1)
