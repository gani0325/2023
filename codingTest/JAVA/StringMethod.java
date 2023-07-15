import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        String str = "My name is gani";

        // 길이 반환
        System.out.println(str.length());

        // 빈 문자열 체크
        System.out.println(str.isEmpty());

        // 문자 찾기
        System.out.println(str.charAt(0)); // 'M' -> 문자 반환
        System.out.println(str.indexOf("a")); // 0 -> 인덱스 반환
        System.out.println(str.lastIndexOf("i")); // i -> 마지막으로 문자가 속한 인덱스 반환
    }
}