import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        List<String> list2 = new ArrayList<>();

        // 리스트 차집합
        list.removeAll(list2); // list에서 list2에 있는 모든 값을 삭제

        // 리스트 교집합
        list.retainAll(list2); // list에서 list2에 있는 값을 제외한 모든 값을 삭제

        // 리스트 비우기
        list.clear();

        // 리스트 비어있는지 체크
        System.out.println(list.isEmpty());

        // 리스트 길이
        System.out.println(list.size());
    }
}