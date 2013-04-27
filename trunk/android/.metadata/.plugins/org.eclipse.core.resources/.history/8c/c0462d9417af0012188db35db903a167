package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer.RequestTask.TemperatureCallback;

public class MainActivity extends Activity implements TemperatureCallback {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
    
    public void retrieveTemperatureFromServer () {
    	//new RequestTask().execute("http://www.server.com/pathToRequestScript");
    }

    /**
     * receives temperature from http request
     * @param temp - int value, holding the current temperature
     */
	@Override
	public void temperatureCallback(int temp) {
		// TODO Auto-generated method stub
		
	}

	
}
