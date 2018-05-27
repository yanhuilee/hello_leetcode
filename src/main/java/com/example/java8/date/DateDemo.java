package com.example.java8.date;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.TemporalAccessor;
import java.time.temporal.TemporalAdjusters;

/**
 * Created by lee on 05/27/18.
 */
public class DateDemo {
    
    // 日期调整器
    public static void main(String[] args) {
        // 每月每一个星期二
        LocalDate firstTuesday = LocalDate.of(2018, 5, 1)
                .with(TemporalAdjusters.nextOrSame(DayOfWeek.TUESDAY));
        System.out.println("firstTuesday = " + firstTuesday);

        // 本地时间
        LocalTime rightNow = LocalTime.now();

        // 格式化和解析
        TemporalAccessor apollo_launch = null;
        String formatted = DateTimeFormatter.ISO_DATE_TIME.format(apollo_launch);
    }
}
