import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.annotation.ElementType;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
// sayBefore 如果添加了这个注解，方法在执行之前会先输出value中的值
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD) 
@interface SayBefore {
    String value() default "\\(^o^)/~";
}
// sayAfter 如果添加了这个注解，方法在执行之后会输出value中的值
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD) 
@interface SayAfter {
    String value() default "o(╥﹏╥)o";
}
// 定义服务接口
interface MyService {
    @SayBefore("Hello")
    @SayAfter("Bye")
    void doSomething();
}

// 实现服务接口
class MyServiceImpl implements MyService {
    @Override
    public void doSomething() {
        System.out.println("Doing something in MyServiceImpl.");
    }
}

// 定义日志切面处理器
class LoggingInvocationHandler implements InvocationHandler {
    private final Object target;

    public LoggingInvocationHandler(Object target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 如果有@SayBefore注解，则执行日志记录操作
        if (method.isAnnotationPresent(SayBefore.class)) {
            SayBefore sayBefore = method.getAnnotation(SayBefore.class);
            System.out.println(sayBefore.value());
        }
        
        // 执行目标方法
        Object result = method.invoke(target, args);
        
        // 如果有@SayAfter注解，则执行日志记录操作
        if (method.isAnnotationPresent(SayAfter.class)) {
            SayAfter sayAfter = method.getAnnotation(SayAfter.class);
            System.out.println(sayAfter.value());
        }
        
        return result;
    }
}

// 主程序
public class AOPExample {
    public static void main(String[] args) {
        // 创建服务实现类的实例
        MyService myService = new MyServiceImpl();
        
        // 创建一个 InvocationHandler
        LoggingInvocationHandler handler = new LoggingInvocationHandler(myService);
        
        // 创建代理对象
        MyService proxy = (MyService) Proxy.newProxyInstance(
            myService.getClass().getClassLoader(),
            myService.getClass().getInterfaces(),
            handler
        );
        
        // 使用代理对象
        proxy.doSomething();
    }
}
