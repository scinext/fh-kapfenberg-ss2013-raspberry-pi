import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

/**
 * A server program which accepts requests from clients to
 * capitalize strings.  When clients connect, a new thread is
 * started to handle an interactive dialog in which the client
 * sends in a string and the server thread sends back the
 * capitalized version of the string.
 *
 * The program is runs in an infinite loop, so shutdown in platform
 * dependent.  If you ran it from a console window with the "java"
 * interpreter, Ctrl+C generally will shut it down.
 */
public class CapitalizeServer {
	
	public static String SENSOR_STRAWBERRY_NAME = "Strawberry";
	public static String SENSOR_RASPBERRY_NAME = "Raspberry";
	public static String SENSOR_BLACKBERRY_NAME = "Blackberry";
	public static String SENSOR_BLUEBERRY_NAME = "Blueberry";
	
	private Sensors sensors;

	public static CapitalizeServer main;


    public static void main(String[] args) throws Exception {
    	
    	main = new CapitalizeServer();
    	main.setSensors(new Sensors());
    	
    	main.sensors.startCreatingTemperatureValues();
    	
        System.out.println("The capitalization server is running.");
        int clientNumber = 0;
        ServerSocket listener = new ServerSocket(5000);
        try {
            while (true) {
                new Capitalizer(listener.accept(), clientNumber++).start();
            }
        } finally {
            listener.close();
        }
    }

    public Sensors getSensors() {
		return sensors;
	}

	public void setSensors(Sensors sensors) {
		this.sensors = sensors;
	}

    private static class Capitalizer extends Thread {
        private Socket socket;
        private int clientNumber;

        public Capitalizer(Socket socket, int clientNumber) {
            this.socket = socket;
            this.clientNumber = clientNumber;
            log("New connection with client# " + clientNumber + " at " + socket);
        }

        /**
         * Services this thread's client by first sending the
         * client a welcome message then repeatedly reading strings
         * and sending back the capitalized version of the string.
         */
        public void run() {
            try {

                // Decorate the streams so we can send characters
                // and not just bytes.  Ensure output is flushed
                // after every newline.
                BufferedReader in = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

                // Send a welcome message to the client.
                //out.println("Hello, you are client #" + clientNumber + ".");
                //out.println("Enter a line with only a period to quit\n");

                // Get messages from the client, line by line; return them
                // capitalized
                while (true) {
                    String input = in.readLine();
                    
                    String response = createXmlResponseForSensor(SENSOR_STRAWBERRY_NAME);
                    log(response);
                    
                    //out.println(response);
                    
                    if (input == null || input.equals(".")) {
                        break;
                    }
                    
                    else if (input.equals("getTemp:Strawberry")) {
                    	out.println(createXmlResponseForSensor(SENSOR_STRAWBERRY_NAME));
                    }
                    else if (input.equals("getTemp:Raspberry")) {
                    	out.println(createXmlResponseForSensor(SENSOR_RASPBERRY_NAME));
                    }
                    else if (input.equals("getTemp:Blackberry")) {
                    	out.println(createXmlResponseForSensor(SENSOR_BLACKBERRY_NAME));
                    }
                    else if (input.equals("getTemp:Blueberry")) {
                    	out.println(createXmlResponseForSensor(SENSOR_BLUEBERRY_NAME));
                    }
                    
                }
            } catch (IOException e) {
                log("Error handling client# " + clientNumber + ": " + e);
            } finally {
                try {
                    socket.close();
                } catch (IOException e) {
                    log("Couldn't close a socket, what's going on?");
                }
                log("Connection with client# " + clientNumber + " closed");
            }
        }

        /**
         * Logs a simple message.  In this case we just write the
         * message to the server applications standard output.
         */
        private void log(String message) {
            System.out.println(message);
        }
        
        public String createXmlResponseForSensor (String sensorName) {
        	String response = "<response from='$(from)' id='$(id)' to='$(to)'>" +
        			"<sensors>";
        	
        	HashMap<String, String> sensorMap = null; 
        	
        	if (sensorName.equals(SENSOR_STRAWBERRY_NAME)) {
        		sensorMap = main.getSensors().StrawberryMap;
        	}
        	else if (sensorName.equals(SENSOR_RASPBERRY_NAME)) {
        		sensorMap = main.getSensors().RaspberryMap;
        	}
        	else if (sensorName.equals(SENSOR_BLACKBERRY_NAME)) {
        		sensorMap = main.getSensors().BlackberryMap;
        	}
        	else if (sensorName.equals(SENSOR_BLUEBERRY_NAME)) {
        		sensorMap = main.getSensors().BlueberryMap;
        	}
        	
        	Iterator<Entry<String, String>> it = sensorMap.entrySet().iterator();
            while (it.hasNext()) {
                Map.Entry pairs = (Map.Entry)it.next();
                response += "<sensor errorCode='0'" + " " + "name='"+ sensorName + "' " + "timestamp='"+ pairs.getKey() + "' " + "value='" + pairs.getValue() + "'/>";
            }
        	
        	response += "</sensors>";
        	response += "</response>";
        	return response;
        }
    }
}