class AML {
    protected void display() {
        System.out.println("Hello");
    }

    public void add(int a, int b) {
        int c = a + b;
        System.out.println(c);
    }
}

class Shivam extends AML {
    public void display() {
        System.out.println("From child");
    }

    public void add(int x, int y) {
        int z = x + y;
        System.out.println(z);
    }

    public static void main(String args[]) {
        AML a1 = new AML();
        Shivam b1 = new Shivam();
        a1.display();
        a1.add(50, 60);
        b1.display();
        b1.add(10, 20);
    }
}