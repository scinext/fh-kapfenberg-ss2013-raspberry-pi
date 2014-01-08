package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class SocketClient {
	private Socket socket;

	private int serverPort;
	private String serverIP;
	
	private BufferedReader in;
    private PrintWriter out;
	
	//private static final int SERVERPORT = 5000;
	//private static final String SERVER_IP = "10.0.2.2";
	
	//constructor sets serverPort and serverIP
	//starts socket client
	public SocketClient (int serverPort, String serverIP) {
		setServerPort(serverPort);
		setServerIP(serverIP);
		
		try {
			InetAddress serverAddr = InetAddress.getByName(serverIP);

			setSocket(new Socket(serverAddr, serverPort));
			
			in = new BufferedReader(
	                new InputStreamReader(socket.getInputStream()));
			
	        out = new PrintWriter(socket.getOutputStream(), true);
			

		} catch (UnknownHostException e1) {
			e1.printStackTrace();
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		
	}
	
	public String sendRequest (String request) throws IOException {
		System.out.println("Client is sending request->" + request);
		
		//send request through socket
		out.println(request);
		
        String response;

        try {
            response = in.readLine();
            if (response == null || response.equals("")) {
                  System.exit(0);
              }
        } catch (IOException ex) {
               response = "Error: " + ex;
        }
	        
	    out.println(".");
	        
	    return response;
        
	}

	public Socket getSocket() {
		return socket;
	}



	public void setSocket(Socket socket) {
		this.socket = socket;
	}



	public int getServerPort() {
		return serverPort;
	}



	public void setServerPort(int serverPort) {
		this.serverPort = serverPort;
	}



	public String getServerIP() {
		return serverIP;
	}



	public void setServerIP(String serverIP) {
		this.serverIP = serverIP;
	}
}

