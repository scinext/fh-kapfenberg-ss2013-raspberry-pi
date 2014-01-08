import java.util.HashMap;
import java.util.Timer;
import java.util.TimerTask;


public class Sensors {
	public static String SENSOR_STRAWBERRY_NAME = "Strawberry";
	public static String SENSOR_RASPBERRY_NAME = "Raspberry";
	public static String SENSOR_BLACKBERRY_NAME = "Blackberry";
	public static String SENSOR_BLUEBERRY_NAME = "Blueberry";
	
	public HashMap<String, String> StrawberryMap = new HashMap<>();
	public HashMap<String, String> RaspberryMap = new HashMap<>();
	public HashMap<String, String> BlackberryMap = new HashMap<>();
	public HashMap<String, String> BlueberryMap = new HashMap<>();
	

	public void startCreatingTemperatureValues () {
			TimerTask action = new TimerTask() {
			
			public void run() {
				addTemperatureForSensor(SENSOR_STRAWBERRY_NAME);
				addTemperatureForSensor(SENSOR_RASPBERRY_NAME);
				addTemperatureForSensor(SENSOR_BLACKBERRY_NAME);
				addTemperatureForSensor(SENSOR_BLUEBERRY_NAME);
			}

		};
		
		Timer caretaker = new Timer();
		caretaker.schedule(action, 0, 1000);
	}
	
	private void addTemperatureForSensor (String sensorName) {
		long timestamp = System.currentTimeMillis()/1000;
		//System.out.println("creating value at timestamp:" + timestamp);
		
		
		if (sensorName.equals(SENSOR_STRAWBERRY_NAME)) {
			StrawberryMap.put(String.valueOf(timestamp), String.valueOf(temperatureBetweenValues(18.0f, 20.0f)));
		}
		else if (sensorName.equals(SENSOR_RASPBERRY_NAME)) {
			RaspberryMap.put(String.valueOf(timestamp), String.valueOf(temperatureBetweenValues(15.0f, 17.0f)));
		}
		else if (sensorName.equals(SENSOR_BLACKBERRY_NAME)) {
			BlackberryMap.put(String.valueOf(timestamp), String.valueOf(temperatureBetweenValues(30.0f, 35.0f)));
		}
		else if (sensorName.equals(SENSOR_BLUEBERRY_NAME)) {
			BlueberryMap.put(String.valueOf(timestamp), String.valueOf(temperatureBetweenValues(0.0f, 10.0f)));
		}
	}
	
	private float temperatureBetweenValues (final float lower, final float upper) {
		return (float) ((Math.random() * (upper - lower)) + lower);
	}
}
