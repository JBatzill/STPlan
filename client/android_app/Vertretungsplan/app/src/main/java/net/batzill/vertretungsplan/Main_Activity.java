package net.batzill.vertretungsplan;

import android.app.ActionBar;
import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.view.Gravity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.MotionEvent;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.EditText;
import android.widget.ExpandableListView;
import android.widget.LinearLayout;
import android.widget.Spinner;
import android.widget.Toast;


public class Main_Activity extends Activity {

    private final int sdkVersion = Build.VERSION.SDK_INT;

    private LinearLayout.LayoutParams paramExpanded = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT, 10f);
    private LinearLayout.LayoutParams paramCollapsed_1 = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT, 1f);
    private LinearLayout.LayoutParams paramCollapsed_2 = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT, 2f);


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_);

        ActionBar actionBar = getActionBar();
        actionBar.setDisplayOptions(ActionBar.DISPLAY_SHOW_CUSTOM);

        LinearLayout actionBarLayout = (LinearLayout)getLayoutInflater().inflate(R.layout.actionbar_layout, null);
        ActionBar.LayoutParams params = new ActionBar.LayoutParams(
                ActionBar.LayoutParams.MATCH_PARENT,
                ActionBar.LayoutParams.MATCH_PARENT,
                Gravity.LEFT);

        actionBar.setCustomView(actionBarLayout, params);
        actionBar.setDisplayHomeAsUpEnabled(false);

        this.setListener();
    }

    private void setListener() {
        final LinearLayout invis = (LinearLayout)this.findViewById(R.id.invisible);

        final EditText txt_class = (EditText)this.findViewById(R.id.txt_class);
        txt_class.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View v, boolean hasFocus) {
                if (hasFocus) {
                    txt_class.setLayoutParams(paramExpanded);
                    if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
                        txt_class.setTranslationZ(20);
                    }
                } else {
                    txt_class.setLayoutParams(paramCollapsed_1);
                    if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
                        txt_class.setTranslationZ(0);
                    }
                }
            }
        });

        //----------------------------------------------------------------------------------------------------

        final AutoCompleteTextView txt_school = (AutoCompleteTextView)this.findViewById(R.id.txt_school);

        String[] countries = {"abcd", "efg", "ironman", "whatever", "superman"};
        ArrayAdapter<String> adapter_school = new ArrayAdapter<String>(this, R.layout.acomplete_drop_item_normal,countries);
        txt_school.setAdapter(adapter_school);

        txt_school.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View v, boolean hasFocus) {
                if (hasFocus) {
                    txt_school.setLayoutParams(paramExpanded);
                    if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
                        txt_school.setTranslationZ(20);
                    }
                } else {
                    txt_school.setLayoutParams(paramCollapsed_2);
                    if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
                        txt_school.setTranslationZ(0);
                    }
                }
            }
        });

        //----------------------------------------------------------------------------------------------------
        final Spinner sp_day = (Spinner)this.findViewById(R.id.sp_day);

        ArrayAdapter<CharSequence> adapter_day = ArrayAdapter.createFromResource(this,
                R.array.days_array, R.layout.spinner_item_normal);
        adapter_day.setDropDownViewResource(R.layout.spinner_drop_item_normal);
        sp_day.setAdapter(adapter_day);

        sp_day.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                invis.requestFocus();
                return false;
            }
        });

        sp_day.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main_, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    public void test(View view){
        Toast.makeText(this, "Hello World", Toast.LENGTH_LONG).show();
    }
}
