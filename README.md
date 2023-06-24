# cnbc-algorithms-analysis-and-design-from-scratch
Cloud Native Base Camp algorithms course assignments

---

# Insertion sort
- Starting from array[1] and this is the key to commpare **we start from the second element in the array.**
- Loop over the array with `(i = 1 ;i < array.length; i++)`.
- Start the nested loop with `j = i - 1` and use it backwards to back to `array[0]`.
- Inside this nested loop test the following condition
    - `array[j] > key` then push the value at array[j] forward `array[j+1] = array[j]`.
    - else breack the loop.
- Finaly shift the `key` value with `array[j+1] = key` in side the body of the first loop.

```java
// Java Code
public static int[] insertionSort(int[] array){
    // start loop over the array from the second element
    for(int i = 1; i < array.length; i++){
        // get the key for comparing.
        int key = array[i];
        int j;
        // loop over the array backwords.
        for(j = i - 1; j >= 0; j--){
            // compare the key with the previous elements
            if (array[j] > key)
                // push big values forward.
                array[j+1] = array[j];
            else
                break;
        }
        // put the key in the right position.
        array[j+1] = key;
    }
    return array;
}
```
---
