import java.rmi.Naming;
import java.util.Scanner;

public class StringClient {

    public static void main(String[] args) {

        try {

            // Lookup server object-- Registry, give me StringService object
            StringInterface obj =
                    (StringInterface) Naming.lookup("rmi://localhost/StringService");

            Scanner sc = new Scanner(System.in);

            // Input strings
            System.out.print("Enter first string: ");
            String str1 = sc.nextLine();

            System.out.print("Enter second string: ");
            String str2 = sc.nextLine();

            // Call remote method
            String result = obj.concatenate(str1, str2);

            // Display output
            System.out.println("Concatenated String: " + result);

        } catch (Exception e) {

            System.out.println("Client Error: " + e);
        }
    }
}