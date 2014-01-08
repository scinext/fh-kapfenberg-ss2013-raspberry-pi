/* <?xml version="1.0" encoding="utf-8"?>
 * <response from="$(from)" id="$(id)" to="$(to)">
 * 	<sensors>
 *    	<sensor errorCode="0" name="Strawberry" timestamp="1367168460" value="20.12"/>
 *   	<sensor errorCode="0" name="Raspberry" timestamp="1367168460" value="30"/>
 *   	<sensor errorCode="1" name="Banana" timestamp="1367168467" value="27.132"/>
 *   	<sensor errorCode="0" name="Blackberry" timestamp="1367168461" value="27.132"/>
 * 	</sensors>
 * </response>
 */

package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer.xmlparsing;

import java.util.ArrayList;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;


/**
 * Parses xml
 * Allocates new sensor models and sets values
 */
public class ResponseXMLHandler extends DefaultHandler {
	
	public static final String ATTR_ERRORCODE = "errorCode";
	public static final String ATTR_NAME = "name";
	public static final String ATTR_TIMESTAMP = "timestamp";
	public static final String ATTR_VALUE = "value";

	Boolean currentElement = false;
	String currentValue = "";
	TemperatureSensor sensor = null;
	
	private ArrayList<TemperatureSensor> sensorsList = new ArrayList<TemperatureSensor>();

	public ArrayList<TemperatureSensor> getItemsList() {
		return sensorsList;
	}

	// Called when tag starts
	@Override
	public void startElement(String uri, String localName, String qName,
			Attributes attributes) throws SAXException {

		currentElement = true;
		currentValue = "";

		if (localName.equals("sensor")) {
			sensor = new TemperatureSensor();
			sensor.setErrorCode(attributes.getValue(ATTR_ERRORCODE));
			sensor.setName(attributes.getValue(ATTR_NAME));
			sensor.setTimestamp(Long.parseLong(attributes.getValue(ATTR_TIMESTAMP)));
			sensor.setValue(Double.parseDouble(attributes.getValue(ATTR_VALUE)));
		}

	}

	// Called when tag closing
	@Override
	public void endElement(String uri, String localName, String qName)
			throws SAXException {

		currentElement = false;

		if (localName.equals("sensor")) {
			
			sensorsList.add(sensor);
			
		}
	}

	// Called to get tag characters
	@Override
	public void characters(char[] ch, int start, int length)
			throws SAXException {

		if (currentElement) {
			currentValue = currentValue + new String(ch, start, length);
		}
	}

}