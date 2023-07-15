import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        String str = "apple";

        // 문자 동일 여부 판단
        // 자바 string의 경우, 클래스로써 Call by Reference형태로 생성 시 주소값이 부여
        // => String타입을 선언했을때는 같은 값을 부여하더라도 서로간의 주소값이 다르다.
        // => 값 비교로는 equals를 사용
        System.out.println(str.equals("apple"));

        // 문자 비교
        /**
         * str과 같으면 0
         * str이 사전순으로 앞이면 -1
         * str이 사전순으로 뒤면 1
         * str이 마지막 문자만 다르면, 마지막 문자의 사전순 차이 반환
         */
        System.out.println(str.compareTo("applq"));

        // 문자 포함 여부 판단
        System.out.println(str.contains("app"));

        // 문자 <-> 숫자 변환
        System.out.println(Integer.parseInt("100")); // 문자열 "100"을 숫자 100으로 변환
        System.out.println(Integer.toString(100)); // 숫자 100을 문자열 "100"으로 변환
    }
}