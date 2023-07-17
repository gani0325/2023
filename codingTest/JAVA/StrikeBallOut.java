import java.util.Random;
import java.util.Scanner;
import java.util.*;
import java.io.*;

public class Problem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        // 랜덤으로 만든 숫자 3자리
        int[] RandomNumber = generateRandom(3, random);
        // 비교를 위해 문자열로 만들겠음
        String StringRandomNumber = Integer.toString(RandomNumber);

        int num = 0;

        while (true) {
            // 게임 시작 (추측값)
            String guess = scanner.nextLine();

            // 도전횟수
            num++;

            // 스트라이크, 볼, 아웃이 담긴 배열 만들어줌
            int[] result = StrikeBallOut(StringRandomNumber, guess);

            int strikes = result[0];
            int balls = result[1];
            int outs = result[2];

            System.out.println(num + " - S:" + strikes + ", B:" + balls + ", O:" + outs);

            // 정답을 맞출 때까지 게임이 진행
            if (strikes == 3) {
                System.out.println(num + " - S:" + strikes + ", B:" + balls + ", O:" + outs + " (종료)");
                break;
            }
        }
    }

    // 1) Random 을 통해 3자리의 랜덤값을 만들어주는 메소드
    public static int[] generateRandom(int length, Random random) {
        int[] digits = new int[length];

        for (int i = 0; i < length; i++) {
            digits[i] = random.nextInt(10);
        }
        return digits;
    }

    // 2) 스트라이크, 볼, 아웃 개수 계산해줌
    // N - 도전 횟수 S:n - 숫자와 위치가 모두 같은 경우(개수) B:n - 숫자가 다른 자리에 있는 경우(개수) O:n - 숫자가 없는
    // 경우(개수)
    public static int[] StrikeBallOut(String random, String game) { // RandomNumber, GameNumber
        int strikes = 0;
        int balls = 0;
        int outs = 0;

        for (int i = 0; i < random.length; i++) {
            if (random.charAt(i) == game.charAt(i)) {
                strikes++;
                // 숫자 배열에서 특정 숫자가 포함되어 있는지 여부를 확인
            } else if (random.contains(String.valueOf(game.charAt(i)))) {
                balls++;
            } else {
                outs++;
            }
        }

        return new int[] { strikes, balls, outs };
    }
}
