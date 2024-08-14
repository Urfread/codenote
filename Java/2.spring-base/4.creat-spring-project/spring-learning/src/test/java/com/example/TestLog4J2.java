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
