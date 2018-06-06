package com.algo.demo100;

/**
 * 河内之塔
 * Created by lee on 06/05/18.
 */
public class TowersOfHanoi {

    public static void main(String[] args) {
        int n = 3;
        hanoi(n, 'A', 'B', 'C');
    }

    public static void hanoi(int n, char A, char B, char C) {
        // 如果柱子标为ABC，要由A搬至C，在只有一个盘子时，就将它直接搬至C，
        // 当有两个盘子，就将B柱当作辅助：A->B、 A ->C、B->C这三个步骤
        if (1 == n) {
            System.out.println(String.format("Move sheet %d from %c to %c", new Object[]{n, A, C}));
        } else {
            hanoi(n - 1, A, C, B);
            System.out.println(String.format("Move sheet %d from %c to %c", new Object[]{n, A, C}));
            hanoi(n - 1, B, A, C);
        }
    }
}
