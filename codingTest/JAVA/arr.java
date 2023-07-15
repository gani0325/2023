import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        String[] arr = { "Apple", "Kiwi", "Orange", "Banana", "Watermelon", "Cherry" };

        // 문자열 길이로 비교하는 Comparator를 구현
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.length() - s2.length();
            }
        });

        System.out.println("문자열 길이 순서로 정렬 : " + Arrays.toString(arr));
    }
}