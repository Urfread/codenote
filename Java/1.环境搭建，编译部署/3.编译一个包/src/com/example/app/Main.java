package com.example.app;

import com.example.utils.Greeting;
import com.example.utils.MathUtils;

public class Main {
    public static void main(String[] args) {
        Greeting greeting = new Greeting("Hello from Greeting class!");
        greeting.printMessage();
        int sum = MathUtils.add(5, 3);
        System.out.println("Sum: " + sum);
    }
}
