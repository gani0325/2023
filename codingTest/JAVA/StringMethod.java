import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        String str = "My name is gani";

        // 문자 자르기
        System.out.println(str.substring(1, 3)); // 인덱스 1 이상 3 미만 위치의 문자열 반환
        System.out.println(str.substring(3)); // 인덱스 3 미만 위치의 문자열 반환

        // 문자 치환(바꾸기)
        // replace([기존문자], [바꿀문자])
        System.out.println(str.replace('g', 'n')); // 모든 [기존 문자]를 [바꿀 문자]로 치환

        // replaceAll([정규식], [바꿀문자])
        System.out.println(str.replaceAll(".", "/")); // "/////" -> 정규식에 맞춰 문자 치환 (정규식 "." 은 모든 문자를 의미)

        String str2 = "gani";
        // replaceFirst([기존문자], [바꿀문자])
        System.out.println(str2.replaceFirst('i', 'p')); // 여러 문자 중 첫번째만 치환
    }
}