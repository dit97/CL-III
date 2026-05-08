import java.rmi.Naming;
import java.util.Map;
import java.util.Scanner;

public class HotelClient {

    public static void main(String[] args) {
        try {
            // checks in register for object name hotelService
            HotelServiceInterface hotelService =
                (HotelServiceInterface) Naming.lookup("rmi://localhost:5000/HotelService");

            Scanner sc = new Scanner(System.in);

            while (true) {
                System.out.println("\n1. Book Room");
                System.out.println("2. Cancel Booking");
                System.out.println("3. Show Booked Rooms");
                System.out.println("4. Exit");
                System.out.print("Enter choice: ");

                int choice = sc.nextInt();
                sc.nextLine();

                switch (choice) {

                    case 1:
                        System.out.print("Enter guest name: ");
                        String name = sc.nextLine();

                        System.out.print("Enter room number: ");
                        int room = sc.nextInt();

                        if (hotelService.bookRoom(name, room))
                            System.out.println("Room booked successfully!");
                        else
                            System.out.println("Room already booked!");
                        break;

                    case 2:
                        System.out.print("Enter guest name: ");
                        String g = sc.nextLine();

                        if (hotelService.cancelBooking(g))
                            System.out.println("Booking canceled!");
                        else
                            System.out.println("Not found!");
                        break;

                    case 3:
                        Map<Integer, String> rooms =
                            hotelService.showBookedRoomDetails();

                        System.out.println("Booked Rooms:");
                        for (Map.Entry<Integer, String> e : rooms.entrySet()) {
                            System.out.println("Room " + e.getKey() + " -> " + e.getValue());
                        }
                        break;

                    case 4:
                        System.out.println("Exiting...");
                        System.exit(0);

                    default:
                        System.out.println("Invalid choice");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
