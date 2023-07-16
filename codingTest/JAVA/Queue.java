import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        // 큐에 요소 추가(enqueue)
        queue.add(1);
        queue.add(4);
        queue.add(5);
        System.out.println(queue);

        // 큐에서 요소 제거(dequeue)
        queue.remove(4); // 문제 상황에서 예외 발생
        System.out.println(queue);

        // 큐 비우기
        queue.clear();
        System.out.println(queue);

        // 큐의 최전방 요소 확인
        queue.element(); // 문제 상황에서 예외 발생
        queue.peek(); // 문제 상황에서 null 리턴
    }
}