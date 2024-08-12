public class Singleton {

    // 1. 私有静态实例变量，唯一实例
    private static Singleton instance;

    // 2. 私有构造函数，防止外部实例化
    private Singleton() {
        // 初始化代码
    }

    // 3. 提供公共的静态方法获取实例
    public static Singleton getInstance() {
        if (instance == null) {
            // 同步代码块以避免多线程环境下的问题
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }

    // 4. 示例方法
    public void showMessage() {
        System.out.println("Hello from Singleton!");
    }
    public static void main(String[] args) {
        // 获取唯一实例
        Singleton singleton = Singleton.getInstance();

        // 调用示例方法
        singleton.showMessage();
    }
}
