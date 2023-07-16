// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        // 문자열 추가
        System.out.println(sb.append("apple")); // "apple"

        // 특정 인덱스에 문자 삽입
        System.out.println(sb.insert(2, "oo")); // "apoople"

        // 문자열 삭제
        System.out.println(sb.delete(0, 2)); // "oople"

        // 특정 인덱스의 문자 삭제
        System.out.println(sb.deleteCharAt(2)); // "oole"

    }
}