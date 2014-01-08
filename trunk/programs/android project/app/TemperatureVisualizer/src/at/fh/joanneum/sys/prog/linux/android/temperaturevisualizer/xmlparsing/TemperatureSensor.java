package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer.xmlparsing;

/**
 * Sensor model class, holding relevant sensor values
 */

public class TemperatureSensor {

	private String errorCode;
	private String name;
	private long timestamp;
	private double value;
	
	public String getErrorCode() {
		return errorCode;
	}
	public void setErrorCode(String errorCode) {
		this.errorCode = errorCode;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public long getTimestamp() {
		return timestamp;
	}
	public void setTimestamp(long timestamp) {
		this.timestamp = timestamp;
	}
	public double getValue() {
		return value;
	}
	public void setValue(double value) {
		this.value = value;
	}


}