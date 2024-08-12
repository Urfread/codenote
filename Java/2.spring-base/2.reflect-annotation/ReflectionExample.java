import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class ReflectionExample {
    public static void main(String[] args) {
        try {
            // 获取 Class 对象
            Class<?> clazz = Class.forName("java.util.ArrayList");

            // 获取构造函数并创建实例
            Constructor<?> constructor = clazz.getConstructor();
            Object instance = constructor.newInstance();

            // 调用方法
            Method addMethod = clazz.getMethod("add", Object.class);
            addMethod.invoke(instance, "Hello Reflection");

            // 获取并调用 toString 方法
            Method toStringMethod = clazz.getMethod("toString");
            String result = (String) toStringMethod.invoke(instance);
            System.out.println(result); // 输出: [Hello Reflection]

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
