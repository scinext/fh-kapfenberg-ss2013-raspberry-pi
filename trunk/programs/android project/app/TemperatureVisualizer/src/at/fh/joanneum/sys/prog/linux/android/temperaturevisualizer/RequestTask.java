package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer;

import java.io.IOException;

import android.app.Activity;
import android.os.AsyncTask;

public class RequestTask extends AsyncTask<String, String, String>{
	
	TemperatureServerResponse response;
	
	public interface TemperatureServerResponse {
	    public void temperatureServerResponse (String response) throws IOException;
	}
	
	public RequestTask (Activity activity) {
		this.response = (TemperatureServerResponse) activity;
	}

	@Override
    protected String doInBackground(String... request) {
        
        SocketClient client = new SocketClient(5000, request[0]);
        
        String serverResponse = null;
        try {
			serverResponse =  client.sendRequest(request[1] + ":" + request[2]);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return serverResponse;
        
        
    }

    @Override
    protected void onPostExecute(String result) {
        super.onPostExecute(result);
        
        //Do anything with response..
        
        System.out.println("Response from server:" + result);
        try {
        	
			response.temperatureServerResponse(result);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}