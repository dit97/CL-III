import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
// make obj remotely accessible
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer extends UnicastRemoteObject implements HotelServiceInterface {

    private Map<Integer, String> bookedRooms;

    public HotelServer() throws RemoteException {
        bookedRooms = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber)
            throws RemoteException {

        if (!bookedRooms.containsKey(roomNumber)) {
            bookedRooms.put(roomNumber, guestName);
            System.out.println("Room " + roomNumber + " booked for " + guestName);
            return true;
        }
        return false;
    }

    @Override
    public synchronized boolean cancelBooking(String guestName)
            throws RemoteException {

        for (Map.Entry<Integer, String> entry : bookedRooms.entrySet()) {
            if (entry.getValue().equals(guestName)) {
                bookedRooms.remove(entry.getKey());
                System.out.println("Booking canceled for " + guestName);
                return true;
            }
        }
        return false;
    }

    @Override
    public synchronized Map<Integer, String> showBookedRoomDetails()
            throws RemoteException {
        return bookedRooms;
    }

    public static void main(String[] args) {
        try {
            HotelServer server = new HotelServer();

            LocateRegistry.createRegistry(5000);
            Naming.rebind("rmi://localhost:5000/HotelService", server);

            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
