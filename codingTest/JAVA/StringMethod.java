import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        String str = "apple";

        // 문자열 분리
        System.out.println(str.split(" ")); // 공백으로 구분된 문자열 str을 분리하여 String[] 배열로 반환
        System.out.println(str.split()); // 띄어쓰기 없는 문자열 str을 한 문자씩 분리하여 String[] 배열로 반환

        // 문자 앞뒤 공백 제거
        System.out.println(str.trim()); // str의 앞뒤 공백을 제거한다. 문자열 사이의 공백은 제거하지 않는다.
    }
}