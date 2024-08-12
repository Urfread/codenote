public class FactoryPatternDemo {
    public static void main(String[] args) {
        // 使用 ConcreteFactoryA 创建 ConcreteProductA
        ProductFactory factoryA = new ConcreteFactoryA();
        Product productA = factoryA.createProduct();
        productA.use();

        // 使用 ConcreteFactoryB 创建 ConcreteProductB
        ProductFactory factoryB = new ConcreteFactoryB();
        Product productB = factoryB.createProduct();
        productB.use();
    }
}
