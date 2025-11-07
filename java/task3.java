import java.util.Scanner;

public class task3 {
    
    public static void main(String[] args) {
        String name = args[0];
        name = "hi";
        //Scanner scanner = new Scanner(System.in);
        //name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");
    }
}

//I believe the bug is from there not being any arguments or input passed. It is index out of bounds because the input doesn't exist. I need to add a scanner for input