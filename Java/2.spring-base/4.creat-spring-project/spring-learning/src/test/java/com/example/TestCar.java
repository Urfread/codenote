package com.example;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.junit.Test;

public class TestCar {

    @Test
    public void testCarWithWheel() {
        // 加载Spring配置文件
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");

        // 获取Car bean
        Car car = (Car) context.getBean("car");

        // 验证Car bean的属性
        System.out.println("Car Name: " + car.getName());
        System.out.println("Wheel Type: " + car.getWheel().getType());

        // 断言以验证测试结果
        assert "Toyota".equals(car.getName());
        assert "All-Season".equals(car.getWheel().getType());
    }
}
