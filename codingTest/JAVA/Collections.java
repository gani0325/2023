import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(0, 3, 2, 1, 5));
        System.out.println(list); // [0, 3, 2, 1, 5]

        // 정수형 List 원소 중 최대, 최소값
        System.out.println(Collections.max(list));
        System.out.println(Collections.min(list));

        // List 정렬
        Collections.sort(list); // 오름차순 (ASC)
        System.out.println(list);
        Collections.sort(list, Collections.reverseOrder()); // 내림차순 (DESC)
        System.out.println(list);

        // List 뒤집기
        Collections.reverse(list);
        System.out.println(list);

        // List 내 원소의 갯수 반환
        System.out.println(Collections.frequency(list, 3));
    }
}