public class ConcreteFactoryA implements ProductFactory {
    @Override
    public Product createProduct() {
        return new ConcreteProductA();
    }
}


