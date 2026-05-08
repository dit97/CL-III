import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class StringServer extends UnicastRemoteObject
        implements StringInterface {

    // Constructor
    protected StringServer() throws RemoteException {
        super();
    }

    // Remote method
    public String concatenate(String str1, String str2)
            throws RemoteException {

        return str1 + " " + str2;
    }

    // Main method
    public static void main(String[] args) {

        try {

            // Create object
            StringServer server = new StringServer();

            // Create registry on port 1099
            java.rmi.registry.LocateRegistry.createRegistry(1099);

            // "Save server object in registry with name StringService"
            Naming.rebind("StringService", server);

            System.out.println("Server is running...");

        } catch (Exception e) {

            System.out.println("Server Error: " + e);
        }
    }
}