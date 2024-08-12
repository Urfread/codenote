package com.example.moduleb;

public class App {
    public static void main(String[] args) {
        MathService mathService = new MathService();
        int result = mathService.performAddition(5, 3);
        System.out.println("Result of addition: " + result);
    }
}
