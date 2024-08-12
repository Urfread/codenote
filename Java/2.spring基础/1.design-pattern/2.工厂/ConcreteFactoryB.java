public class ConcreteFactoryB implements ProductFactory {
    @Override
    public Product createProduct() {
        return new ConcreteProductB();
    }
}