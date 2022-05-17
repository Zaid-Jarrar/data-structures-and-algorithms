# Insertion Sort

### Pesudo Code:

```
Algorithm InsertionSort(int[] arr)
 try:
    FOR i = 1 to arr.length
      int j <-- i - 1

      int temp <-- arr[i]
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
      arr[j + 1] <-- temp
 catch Exception:
 return 'array elements must be integers'
 return arr
```

## Process:
```
Sample Array:
[8,4,23,42,16,15]
```



**First step:** 
```
we enter the for loop then we check if the assign the values of j and temp,

j = i - 1 = 0
temp = arr[1] = 4

enter while loop and check if temp is less than the arr[j] and if j is bigger or equal to 0
looking here at the array, we see that the temp value is less than the value at the jth index, so we enter the while loop.

we then swap the values
arr[j + 1] = arr[j] = 8
after the swap, we see that the value at the jth index is now bigger than the temp value, so we break the loop.
we assign the value at the jth + 1 index  to the temp value.
arr[0] = temp = 4

so it becomes   
[4,8,23,42,16,15]

```


**Second step:** 
```
we check the 8 and 23, 23 is not smaller than 8, so we dont enter the while loop.
the for loop is incremented
and the array stays the same
[4,8,23,42,16,15]
```

**Third step:** 
```
we check the 23 and 42, 42 is not smaller than 23, so we dont enter the while loop.
the for loop is incremented
and the array stays the same

[4,8,23,42,16,15]
```

**Fourth step:** 
```
we check the 42 and 16, 16 is  smaller than 42, so we enter the while loop.
we then swap the values
i = 4
j = j - 1 = 3

temp = 16
we then swap the values
arr[j + 1] = arr[j] = 42
decrement the j by 1
j = j - 1 = 2
j is still bigger than 0, and temp is smaller than arr[j] 23 so we enter the while loop.

we repeat the process until j is less than 0, or temp is bigger than arr[j]
then we assign the value at the jth + 1 index  to the temp value. 16

[4,8,16,23,42,15]
```

**Five step:**
```
we do the same thing we did to the 16 and 42 but with the 42 and 15
to get the final result.

[4,8,16,23,15,42]
```








