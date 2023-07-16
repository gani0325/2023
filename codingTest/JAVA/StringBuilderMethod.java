// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        // 문자열 추가
        System.out.println(sb.append("apple")); // "apple"

        // 특정 인덱스의 문자를 변경
        sb.setCharAt(1, 'e');

        // 문자열 뒤집기
        System.out.println(sb.reverse()); // "elpo"

        // 문자열 절대길이 줄이기
        sb.setLength(2); // "el"

        // 문자열 절대길이 늘이기
        sb.setLength(4); // "el " -> 뒤가 공백으로 채워짐

        System.out.println(sb);
    }
}