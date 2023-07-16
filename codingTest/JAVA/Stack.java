import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        // 요소 추가
        stack.push(1);
        stack.push(2);
        stack.push(3);
        System.out.println(stack);

        // 요소 제거(꺼내기)
        stack.pop(); // 3 빼기

        // 스택 비우기
        stack.clear();
        System.out.println(stack);

        // 스택 크기 체크
        stack.size();

        // 스택이 비어있는지 유무 확인
        stack.empty();

        // 스택에 요소 존재하는지 확인
        stack.contains(1);

        // 스택 최상단 요소 확인
        System.out.println(stack.peek());
    }
}