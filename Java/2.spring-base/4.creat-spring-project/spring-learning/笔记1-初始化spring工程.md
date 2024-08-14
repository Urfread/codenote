先创建一个基础的mvn工程
然后引入基本的spring框架

引入spring-context
```xml
<!-- https://mvnrepository.com/artifact/org.springframework/spring-context -->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.0.2</version>
</dependency>

```
下载依赖
mvn dependency:resolve

创建一个配置文件spirng.xml 可以换名

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd"
>
</beans>
```

定义一个bean

更新一下Junt的版本
```xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
</dependency>
```

专门测试一个类的一个方法
```bash
mvn -Dtest=MyTest#test1 test
```
专门测试一个类
```bash
mvn -Dtest=MyTest test
```

根据之前配置的bean id 获取一个实例
```java
package com.example;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.junit.Test;

public class MyTest {
    @Test
    public void test1() {
        ApplicationContext context = new ClassPathXmlApplicationContext("spring.xml");
        Car car = (Car) context.getBean("car");
        car.setName("BMW");
        System.out.println(car.getName());
    }
}
```