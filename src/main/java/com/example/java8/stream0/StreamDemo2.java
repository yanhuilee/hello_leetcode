package com.example.java8.stream0;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Comparator;
import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Stream;

/**
 * 如何创建 Stream
 * Created by lee on 05/27/18.
 */
public class StreamDemo2 {

    public static void main(String[] args) {
        Stream<String> songs = Stream.of("gently", "down", "the", "stream");

        Stream<Double> randoms = Stream.generate(Math::random);
        // 将数组一部分转换为Stream
//        Arrays.stream(array, from, to)

//        Stream<String> words = localPattern("\\PL+").splitAsStream("");

        // 返回一个包含文件中所有行的流
        try (Stream<String> lines = Files.lines(Paths.get(""))) {
            // 对lines进行处理
        } catch (IOException e) {
            e.printStackTrace();
        }

        // map 操作
        List<String> words = null;
        Stream<String> lowercaseWords = words.stream().map(String::toLowerCase);
        words.stream().map(s -> s.substring(0, 1));

        // sorted()
        Stream<String> longestFirst = words.stream()
                .sorted(Comparator.comparing(String::length).reversed());
    }

    public static Pattern localPattern(String regex) {
        return Pattern.compile(regex);
    }

}
