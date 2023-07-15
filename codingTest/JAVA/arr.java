import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        int[] arr = { 1, 26, 17, 25, 99, 44, 303 };

        // 변수 arr의 순서를 변경해주기 때문에 리턴 값을 다른 변수에 할당할 필요가 없음
        Arrays.sort(arr);
        System.out.println("오름차순 : " + Arrays.toString(arr));
    }
}