import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.Map;

// 自定义注解
@Retention(RetentionPolicy.RUNTIME)
@interface Inject {
}

// 服务类
class ServiceA {
    public void doSomething() {
        System.out.println("ServiceA is doing something!");
    }
}

class ServiceB {
    @Inject
    private ServiceA serviceA;

    public void perform() {
        serviceA.doSomething();
    }
}

// 简单的依赖注入容器
class SimpleDIContainer {
    private Map<Class<?>, Object> container = new HashMap<>();

    public void register(Class<?> clazz) throws Exception {
        Object instance = clazz.getDeclaredConstructor().newInstance();
        container.put(clazz, instance);
    }

    public void injectDependencies() throws Exception {
        for (Object obj : container.values()) {
            Field[] fields = obj.getClass().getDeclaredFields();
            for (Field field : fields) {
                if (field.isAnnotationPresent(Inject.class)) {
                    field.setAccessible(true);// 允许你在反射时访问非公共字段。
                    Object dependency = container.get(field.getType());// 查找并获取容器中与字段类型相匹配的实例，以便进行注入。
                    field.set(obj, dependency);// 将依赖注入到字段中。// 将dependency注入到obj对象的field字段中。
                }
            }
        }
    }
    public <T> T getInstance(Class<T> clazz) {
        // 从依赖注入容器中获取指定类型的实例。
        return clazz.cast(container.get(clazz));
    }
}

public class DependencyInjectionExample {
    public static void main(String[] args) {
        try {
            SimpleDIContainer diContainer = new SimpleDIContainer();
            diContainer.register(ServiceA.class);
            diContainer.register(ServiceB.class);

            diContainer.injectDependencies();

            ServiceB serviceB = diContainer.getInstance(ServiceB.class);
            serviceB.perform(); // Should print: ServiceA is doing something!
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
