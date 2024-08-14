package com.example;

public class Car {
    private String name;
    private Wheel wheel; // 添加 Wheel 类型的属性

    // 使用构造函数注入 Wheel
    public Car(String name, Wheel wheel) {
        this.name = name;
        this.wheel = wheel;
    }
    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public Wheel getWheel() {
        return wheel;
    }
}