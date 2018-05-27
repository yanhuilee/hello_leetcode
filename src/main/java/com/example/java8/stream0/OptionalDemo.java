package com.example.java8.stream0;

import java.util.List;
import java.util.Optional;

/**
 * Optional
 * Created by lee on 05/27/18.
 */
public class OptionalDemo {

    public static void main(String[] args) {
        Optional optional = null;
        optional.orElse("");
//        optional.orElseGet(() - System.getProperty("user.dir"));
//        optional.orElseThrow(IllegalStateException::new);

        // 当前值存在则加入集合
        List results = null;
        optional.ifPresent(v -> results.add(v));
        optional.ifPresent(results::add);
        // 如果相对结果进行处理
        Optional added = optional.map(results::add);


    }
}
