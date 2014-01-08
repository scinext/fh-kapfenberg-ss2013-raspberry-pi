package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer;

import java.io.IOException;
import java.io.StringReader;
import java.util.ArrayList;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.achartengine.ChartFactory;
import org.achartengine.GraphicalView;
import org.achartengine.chart.PointStyle;
import org.achartengine.model.XYMultipleSeriesDataset;
import org.achartengine.model.XYSeries;
import org.achartengine.renderer.XYMultipleSeriesRenderer;
import org.achartengine.renderer.XYSeriesRenderer;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;
import org.xml.sax.XMLReader;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.AssetManager;
import android.graphics.Color;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.LinearLayout;
import android.widget.Toast;
import at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer.RequestTask.TemperatureServerResponse;
import at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer.xmlparsing.ResponseXMLHandler;
import at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer.xmlparsing.TemperatureSensor;

public class MainActivity extends Activity implements TemperatureServerResponse {
	
	private static Context sContext;
	
	private ResponseXMLHandler responseXMLHandler;
	
	private GraphicalView mChart;

    private XYMultipleSeriesDataset mDataset = new XYMultipleSeriesDataset();

    private XYMultipleSeriesRenderer mRenderer = new XYMultipleSeriesRenderer();

    private XYSeries mCurrentSeries;
    
    private XYSeries mStrawberrySeries;
    private XYSeries mRaspberrySeries;
    private XYSeries mBlackberrySeries;
    private XYSeries mBlueberrySeries;

    private XYSeriesRenderer mCurrentRenderer;
    
    private XYSeriesRenderer mCurrentRendererStrawberry;
    private XYSeriesRenderer mCurrentRendererRaspberry;
    private XYSeriesRenderer mCurrentRendererBlackberry;
    private XYSeriesRenderer mCurrentRendererBlueberry;
    
    private static final String TEMP_SENSOR_STRAWBERRY = "Strawberry";
    private static final String TEMP_SENSOR_RASPBERRY = "Raspberry";
    private static final String TEMP_SENSOR_BLACKBERRY = "Blackberry";
    private static final String TEMP_SENSOR_BLUEBERRY = "Blueberry";
   

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        sContext = getApplicationContext(); //set app context
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        
        LinearLayout layout = (LinearLayout) findViewById(R.id.chart);
        if (mChart == null) {
            initChart();
            //addSampleData();
            mChart = ChartFactory.getCubeLineChartView(this, mDataset, mRenderer, 0.3f);
            layout.addView(mChart);
        } else {
            mChart.repaint();
        }
        
        
        
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);

    	
        return true;
    }
    
    
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
    	
	     switch (item.getItemId()) {
	     	case R.id.menu_strawberry:
	     		try {
	    			retrieveTemperatureFromServer(TEMP_SENSOR_STRAWBERRY);
	    		} catch (IOException e) {

	    			e.printStackTrace();
	    		}
	     		break;
	     	case R.id.menu_raspberry:
	     		try {
	    			retrieveTemperatureFromServer(TEMP_SENSOR_RASPBERRY);
	    		} catch (IOException e) {

	    			e.printStackTrace();
	    		}
	     		break;
	     	case R.id.menu_blackberry:
	     		try {
	    			retrieveTemperatureFromServer(TEMP_SENSOR_BLACKBERRY);
	    		} catch (IOException e) {

	    			e.printStackTrace();
	    		}
	     		break;
	     	case R.id.menu_blueberry:
	     		try {
	    			retrieveTemperatureFromServer(TEMP_SENSOR_BLUEBERRY);
	    		} catch (IOException e) {
	    			// TODO Auto-generated catch block

	    		}
	     		break;
	     	case R.id.menu_settings:
	     		callSettings();
	     		break;
	     }
	     
 		
	     
	     return super.onOptionsItemSelected(item);

    }
    
    
    public void callSettings () {
    	Intent myIntent = new Intent(this, SettingsActivity.class);
        startActivity(myIntent);
    }
    
    public void retrieveTemperatureFromServer (String sensorName) throws IOException {
    	//get ip address, user entered in settings and saved to sharedPreferences
		SharedPreferences preferences = getContext().getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);  
		String ipAddress = preferences.getString("ipAddress", null);
		
		if (ipAddress == null) { //user has not set ip address yet
			Toast.makeText(getApplicationContext(), "Bitte IP-Adresse in Settings einstellen!", Toast.LENGTH_SHORT).show();
			return;
		}
	
		new RequestTask(this).execute(ipAddress, "getTemp", sensorName);
	
		
    }

    /**
     * receives response from socket request
     * @param response - string value, holding the response xml
     * @throws IOException 
     */
	@Override
	public void temperatureServerResponse(String response) throws IOException {
		//receives xml response from server (handled in RequestTask)
		AssetManager am = getApplicationContext().getAssets();
    	//InputStream is = am.open("sampleResponse.xml");
    	//String demoServerResponse = new Scanner(is,"UTF-8").useDelimiter("\\A").next();
		System.out.println("Trying to parse response:\n" + response);
    	
    	try {
			SAXParserFactory spf = SAXParserFactory.newInstance();
			SAXParser sp = spf.newSAXParser();
			XMLReader xr = sp.getXMLReader();

			responseXMLHandler = new ResponseXMLHandler();
			xr.setContentHandler(responseXMLHandler);

			final InputSource stringSource = new InputSource(new StringReader(response));  
			
			xr.parse(stringSource);

		} catch (ParserConfigurationException pce) {
			Log.e("SAX XML", "sax parse error", pce);
		} catch (SAXException se) {
			Log.e("SAX XML", "sax error", se);
		} catch (IOException e) {
			e.printStackTrace();
		}
    	
    	ArrayList<TemperatureSensor> sensorList = responseXMLHandler.getItemsList();

		if (null != sensorList && sensorList.size() != 0) {
			
			
			
			
			
			for (int index = 0; index < sensorList.size(); index++) {
				TemperatureSensor sensor = sensorList.get(index);

				/*
				System.out.println(">>>>>>>>>>>>>>>" + index);
				System.out.println("ERROR CODE :: " + sensor.getErrorCode());
				System.out.println("NAME :: " + sensor.getName());
				System.out.println("TIMESTAMP :: " + sensor.getTimestamp());
				System.out.println("VALUE :: " + sensor.getValue());
				*/
				
				XYSeries series = null;
				
				if (sensor.getName().equals(TEMP_SENSOR_STRAWBERRY)) {
					//mStrawberrySeries.clear();
					series = mStrawberrySeries;
				}
				else if (sensor.getName().equals(TEMP_SENSOR_RASPBERRY)) {
					//mRaspberrySeries.clear();
					series = mRaspberrySeries;
				}
				else if (sensor.getName().equals(TEMP_SENSOR_BLACKBERRY)) {
					//mBlackberrySeries.clear();
					series = mBlackberrySeries;
				}
				else if (sensor.getName().equals(TEMP_SENSOR_BLUEBERRY)) {
					//mBlueberrySeries.clear();
					series = mBlueberrySeries;
				}
				
				addDataForVisualization((double)index, sensor.getValue(), series);
			
			}
			mChart.repaint();
		}
	}

	/**
	 * checks, if device is connected to a wireless network
	 * @return true/false - whether connection is available or not
	 */
	public boolean isNetworkAvailable() {
		ConnectivityManager connectivity = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
		if (connectivity == null) {
			return false;
		} else {
			NetworkInfo[] info = connectivity.getAllNetworkInfo();
			if (info != null) {
				for (int i = 0; i < info.length; i++) {
					if (info[i].getState() == NetworkInfo.State.CONNECTED) {
						return true;
					}
				}
			}
		}
		return false;
	}
	
	//chart engine drawing
	private void initChart() {
		mRenderer.setApplyBackgroundColor(true);
        mRenderer.setBackgroundColor(Color.argb(100, 50, 50, 50));
        mRenderer.setAxisTitleTextSize(20);
        mRenderer.setChartTitleTextSize(20);
        mRenderer.setLabelsTextSize(15);
        mRenderer.setLegendTextSize(15);
        mRenderer.setMargins(new int[] { 20, 30, 15, 0 });
        mRenderer.setZoomButtonsVisible(true);
        mRenderer.setPointSize(7);
        mRenderer.setShowGrid(true);
        
        
//        mCurrentSeries = new XYSeries("Blueberry");
//        mDataset.addSeries(mCurrentSeries);
//        mCurrentRenderer = new XYSeriesRenderer();
//        mCurrentRenderer.setPointStyle(PointStyle.CIRCLE);
//        mCurrentRenderer.setFillPoints(true);
//        mRenderer.addSeriesRenderer(mCurrentRenderer);
        
        mStrawberrySeries = new XYSeries("Strawberry");
        mRaspberrySeries = new XYSeries("Raspberry");
        mBlackberrySeries = new XYSeries("Blackberry");
        mBlueberrySeries = new XYSeries("Blueberry");
        
        
        mDataset.addSeries(mStrawberrySeries);
        mDataset.addSeries(mRaspberrySeries);
        mDataset.addSeries(mBlackberrySeries);
        mDataset.addSeries(mBlueberrySeries);
        
        mCurrentRendererStrawberry = new XYSeriesRenderer();
        mCurrentRendererStrawberry.setPointStyle(PointStyle.CIRCLE);
        mCurrentRendererStrawberry.setFillPoints(true);
        mCurrentRendererStrawberry.setColor(Color.RED);
        
        mCurrentRendererRaspberry = new XYSeriesRenderer();
        mCurrentRendererRaspberry.setPointStyle(PointStyle.CIRCLE);
        mCurrentRendererRaspberry.setFillPoints(true);
        mCurrentRendererRaspberry.setColor(Color.MAGENTA);
        
        mCurrentRendererBlackberry = new XYSeriesRenderer();
        mCurrentRendererBlackberry.setPointStyle(PointStyle.CIRCLE);
        mCurrentRendererBlackberry.setFillPoints(true);
        mCurrentRendererBlackberry.setColor(Color.CYAN);
        
        mCurrentRendererBlueberry = new XYSeriesRenderer();
        mCurrentRendererBlueberry.setPointStyle(PointStyle.CIRCLE);
        mCurrentRendererBlueberry.setFillPoints(true);
        mCurrentRendererBlueberry.setColor(Color.BLUE);
        
        
        
        mRenderer.addSeriesRenderer(mCurrentRendererStrawberry);
        mRenderer.addSeriesRenderer(mCurrentRendererRaspberry);
        mRenderer.addSeriesRenderer(mCurrentRendererBlackberry);
        mRenderer.addSeriesRenderer(mCurrentRendererBlueberry);
        
        
    }

	//deprecated
    private void addSampleData() {
        mCurrentSeries.add(1, 22.7f);
        mCurrentSeries.add(2, 22.8f);
        mCurrentSeries.add(3, 22.9f);
        mCurrentSeries.add(3, 21.9f);
        mCurrentSeries.add(3, 21.4f);
    }
    
    private void addDataForVisualization (double x, double y, XYSeries series) {
    	

    	series.add(x, y);
    	
    	System.out.println("adding value:" + y + " at x pos:" + x);
    }
    /**
     * Returns the application context
     *
     * @return application context
     */
    public static Context getContext() {
        return sContext;
    }
}
