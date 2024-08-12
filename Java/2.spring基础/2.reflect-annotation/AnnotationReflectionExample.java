import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.reflect.Field;

// 定义注解
@Retention(RetentionPolicy.RUNTIME)
@interface Inject {
}

// 类和字段上使用注解
class Service {
    @Inject
    private String value;
}

public class AnnotationReflectionExample {
    public static void main(String[] args) {
        try {
            // 获取类对象
            Class<?> clazz = Service.class;
            Field[] fields = clazz.getDeclaredFields();

            // 遍历字段并检查注解
            for (Field field : fields) {
                if (field.isAnnotationPresent(Inject.class)) {
                    System.out.println("Field with @Inject: " + field.getName());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
