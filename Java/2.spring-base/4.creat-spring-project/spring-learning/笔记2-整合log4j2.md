### 注入
#### set注入
引入依赖
```xml
<!-- Log4j2 Core -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>2.19.0</version>
    </dependency>

    <!-- Log4j2 API -->
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-api</artifactId>
        <version>2.19.0</version>
    </dependency>
```

编写配置文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <!-- 定义日志输出目标 -->
    <Appenders>
        <!-- 控制台Appender配置 -->
        <Console name="Console" target="SYSTEM_OUT">
            <!-- PatternLayout定义了日志的输出格式 -->
            <!-- %d{HH:mm:ss.SSS} - 输出时间，格式为小时:分钟:秒.毫秒 -->
            <!-- [%t] - 输出线程名称 -->
            <!-- %-5level - 输出日志级别，宽度为5，不足的部分用空格填充 -->
            <!-- %logger{36} - 输出日志记录器的名称，最多显示36个字符 -->
            <!-- %msg - 输出日志消息 -->
            <!-- %n - 输出换行符 -->
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>
    </Appenders>

    <!-- 定义日志记录器 -->
    <Loggers>
        <!-- 根记录器配置 -->
        <!-- level="info" - 设置根记录器的日志级别为INFO，这意味着INFO级别及以上的日志消息会被记录 -->
        <!-- 关联Console Appender - 将日志消息输出到控制台 -->
        <Root level="info">
            <AppenderRef ref="Console"/>
        </Root>

        <!-- 自定义Logger配置 -->
        <!-- name="com.example" - 指定日志记录器的名称为"com.example"，这意味着只记录属于此包的日志消息 -->
        <!-- level="debug" - 设置自定义记录器的日志级别为DEBUG，这意味着DEBUG级别及以上的日志消息会被记录 -->
        <!-- additivity="false" - 禁用日志的继承，这意味着只有指定的Logger处理日志，不会将日志消息传递到父Logger -->
        <!-- 关联Console Appender - 将日志消息输出到控制台 -->
        <Logger name="com.example" level="debug" additivity="false">
            <AppenderRef ref="Console"/>
        </Logger>
    </Loggers>
</Configuration>


```

记着处理依赖

测试类
```java
package com.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.junit.Test;

public class TestLog4J2 {

    // 创建Log4j2的Logger实例
    private static final Logger logger = LogManager.getLogger(TestLog4J2.class);

    @Test
    public void testLogging() {
        // 记录不同级别的日志消息，用于测试日志配置
        logger.info("This is an INFO level log message.");   // INFO级别日志
        logger.warn("This is a WARN level log message.");    // WARN级别日志
        logger.error("This is an ERROR level log message."); // ERROR级别日志
        logger.debug("This is a DEBUG level log message.");  // DEBUG级别日志

        // 由于JUnit测试框架无法直接捕获和验证控制台输出的日志消息，
        // 这里只是确保日志记录不会引发异常，实际验证通常涉及更多步骤。
    }
}


```
#### 构造注入
```java
package com.example;

public class Car {
    private String name;
    private Wheel wheel; // 添加 Wheel 类型的属性

    // 使用构造函数注入 Wheel
    public Car(String name, Wheel wheel) {
        this.name = name;
        this.wheel = wheel;
    }

    public String getName() {
        return name;
    }

    public Wheel getWheel() {
        return wheel;
    }
}

```

```java
//Wheel无需更改
```

```xml
<!-- 定义Wheel bean -->
<bean id="wheel" class="com.example.Wheel">
    <property name="type" value="All-Season"/>
</bean>

<!-- 定义Car bean，并通过构造函数注入Wheel bean -->
<bean id="car" class="com.example.Car">
    <!-- 使用构造函数注入name属性 -->
    <constructor-arg value="Toyota"/>
    <!-- 使用构造函数注入wheel属性 -->
    <constructor-arg ref="wheel"/>
</bean>
```