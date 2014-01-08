package at.fh.joanneum.sys.prog.linux.android.temperaturevisualizer;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.inputmethod.EditorInfo;
import android.view.inputmethod.InputMethodManager;
import android.widget.TextView;

public class SettingsActivity extends Activity {
	
	public TextView ipAddressTextView;

	@Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        
        setContentView(R.layout.settings_layout);
        
        ipAddressTextView = (TextView)findViewById(R.id.ipAddress);
        
        TextView.OnEditorActionListener actionListener = new TextView.OnEditorActionListener() {

			@Override
			public boolean onEditorAction(TextView ipAddressTextView, int actionId, KeyEvent event) {
				if (actionId == EditorInfo.IME_NULL && event.getAction() == KeyEvent.ACTION_DOWN) { 
				      //save ip address
					  saveIpAddress();
				      //hide the keyboard
				      InputMethodManager imm = (InputMethodManager)getSystemService(Context.INPUT_METHOD_SERVICE);
				      imm.hideSoftInputFromWindow(ipAddressTextView.getWindowToken(), 0);
				}
				return true;
			}
    		
        };
        
        ipAddressTextView.setOnEditorActionListener(actionListener);
        
        //load previously stored ip address
        loadIpAddress();
        
    }
	
	public void loadIpAddress () {
		Context context = MainActivity.getContext();
		SharedPreferences preferences = context.getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);  
		ipAddressTextView.setText(preferences.getString("ipAddress", null));
	}
	
	public void saveIpAddress () {
		Context context = MainActivity.getContext();
		SharedPreferences preferences = context.getSharedPreferences("MyPreferences", Context.MODE_PRIVATE);  
		SharedPreferences.Editor editor = preferences.edit();
		editor.putString("ipAddress", ipAddressTextView.getText().toString());
		editor.commit();
	}
}
