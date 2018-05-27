package com.example.java8.stream0;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

/**
 * 从迭代到Stream
 * Created by lee on 05/27/18.
 */
public class StreamDemo1 {

    public static void main(String[] args) {
        try {
            // 工作空间路径
            String workDir = System.getProperty("user.dir");
            Path path = Paths.get("alice.txt");
            String contents = new String(Files.readAllBytes(path),
                    StandardCharsets.UTF_8);
            // 拆分成单词；非字母被认为是分隔符
            List<String> words = Arrays.asList(contents.split("\\PL+"));

            // 1.
            int count = 0;
            for (String w : words) {
                if (w.length() > 6) {
                    count++;
                }
            }
            System.out.println("count = " + count);
            
            // 2.
            long count2 = words.stream().filter(w -> w.length() > 6).count();
            System.out.println("count2 = " + count2);
            long count3 = words.parallelStream().filter(w -> w.length() > 6).count();
            System.out.println("count3 = " + count3);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
