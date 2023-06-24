import java.util.*;

public class Sorting {

    public static void main(String[] args) {
        int[] array = {1, 6, 3, 9, 1};
        System.out.println(Arrays.toString(insertionSort(array)));
    }

    public static int[] insertionSort(int[] array){
        for(int i = 1; i < array.length; i++){
            int key = array[i];
            int j;
            for(j = i - 1; j >= 0; j--){
                if (array[j] > key)
                    array[j+1] = array[j];
                else
                    break;
            }
            array[j+1] = key;
        }
        return array;
    }
}