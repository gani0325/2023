import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        // asList : 정수 배열을 List로 변환
        int[] temp = { 1, 2, 3, 4 };
        List<Integer> list = new ArrayList<>(Arrays.asList(temp));
        System.out.println(list);

        // toArray : List를 정수 배열로 변환
        List<Integer> list = new ArrayList<>();
        int[] temp = list.stream().mapToInt(x -> x).toArray();
    }
}