import java.util.Scanner;

public class task3 {
    
    public static void main(String[] args) {
        String name = args[0];
        //name = "hi";
        Scanner scanner = new Scanner(System.in);

        //System.out.println("Enter your name: ");
        //String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");

        scanner.close();
    }
}

// No bugs, I hadn't passed the program a name for it to run. I added a scanner that (if uncommented) will ask the user for their name instead of it needing to be passed when the program is ran.
