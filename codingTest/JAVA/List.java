import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        // 요소 삽입
        list.add("one");

        // 특정 인덱스에 요소 삽입
        list.add(0, "zero");
        System.out.println(list);

        // 리스트 병합 (추가되는 리스트가 뒤로 온다)
        list.addAll(list2);

        // 특정 요소의 첫번째 인덱스 반환
        list.indexOf("zero"); // 0

        // 특정 요소의 마지막 인덱스 반환
        System.out.println(list.lastIndexOf("zero"));

        // 특정 인덱스의 값 삭제
        list.remove(0);

        // 첫번째 값 삭제
        list.remove("one");
        System.out.println(list);
    }
}