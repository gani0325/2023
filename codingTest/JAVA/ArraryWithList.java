import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        // asList : 문자열 타입 배열을 List로 변환
        String[] temp = { "apple", "banana", "lemon" };
        List<String> list = new ArrayList<>(Arrays.asList(temp));
        System.out.println(list);

        // toArray : List를 문자열 배열로 변환
        List<String> list = new ArrayList<>();
        String[] temp = list.toArray(new String[list.size()]);
        System.out.println(temp);
    }
}