import java.util.*;
import java.io.*;

// tip: each public class is put in its own file
public class main {
    // tip: arguments are passed via the field below this editor
    public static void main(String[] args) {
        String[] arr = { "Apple", "Kiwi", "Orange", "Banana", "Watermelon", "Cherry" };

        Arrays.sort(arr);

        System.out.println("오름차순 : " + Arrays.toString(arr));
    }
}