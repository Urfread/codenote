import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

// 定义一个注解
@Retention(RetentionPolicy.RUNTIME) // 保留到运行时
@interface MyAnnotation {
    String value() default "default";
}

// 使用注解
@MyAnnotation(value = "example")
public class AnnotationExample {
    public static void main(String[] args) {
        // 获取注解信息
        try {
            Class<?> clazz = AnnotationExample.class;
            MyAnnotation annotation = clazz.getAnnotation(MyAnnotation.class);
            if (annotation != null) {
                System.out.println("Annotation value: " + annotation.value());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
