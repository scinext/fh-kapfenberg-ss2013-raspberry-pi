package com.samir;

import java.util.ArrayList;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class ItemXMLHandler extends DefaultHandler {

	Boolean currentElement = false;
	String currentValue = "";
	Bean item = null;
	private ArrayList<Bean> itemsList = new ArrayList<Bean>();

	public ArrayList<Bean> getItemsList() {
		return itemsList;
	}

	// Called when tag starts
	@Override
	public void startElement(String uri, String localName, String qName,
			Attributes attributes) throws SAXException {

		currentElement = true;
		currentValue = "";

		if (localName.equals("item")) {
			item = new Bean();
		}

	}

	// Called when tag closing
	@Override
	public void endElement(String uri, String localName, String qName)
			throws SAXException {

		currentElement = false;

		if (localName.equals("id")) {
			item.setId(currentValue);
		} else if (localName.equals("title")) {
			item.setTitle(currentValue);
		} else if (localName.equals("desc")) {
			item.setDesc(currentValue);
		} else if (localName.equals("pubDate")) {
			item.setPubDate(currentValue);
		} else if (localName.equals("link")) {
			item.setLink(currentValue);
		} else if (localName.equals("item")) {
			itemsList.add(item);
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
