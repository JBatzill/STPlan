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
import android.view.inputmethod.InputMethodManager;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.Toast;

import net.batzill.vertretungsplan.adapter.ScheduleAdapter;
import net.batzill.vertretungsplan.container.ScheduleEntry;

import java.util.Date;


public class Main_Activity extends Activity {

    private final int sdkVersion = Build.VERSION.SDK_INT;


    private LinearLayout.LayoutParams paramCollapsed_invis = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT, 0f);
    private LinearLayout.LayoutParams paramCollapsed_small = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT, 1f);
    private LinearLayout.LayoutParams paramCollapsed_big = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.MATCH_PARENT, 2f);

    private View focus_taker;
    private LinearLayout actionBarLayout;
    private AutoCompleteTextView txt_school;
    private EditText txt_class;
    private Spinner sp_day;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_);

        ActionBar actionBar = getActionBar();
        actionBar.setDisplayOptions(ActionBar.DISPLAY_SHOW_CUSTOM);

        actionBarLayout = (LinearLayout)getLayoutInflater().inflate(R.layout.actionbar_layout, null);
        ActionBar.LayoutParams params = new ActionBar.LayoutParams(
                ActionBar.LayoutParams.MATCH_PARENT,
                ActionBar.LayoutParams.MATCH_PARENT,
                Gravity.LEFT);

        actionBar.setCustomView(actionBarLayout, params);
        actionBar.setDisplayHomeAsUpEnabled(false);

        focus_taker = (View)this.findViewById(R.id.main_focus_taker);


        this.setListener();
    }

    private void setListener() {

        focus_taker.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View v, boolean hasFocus) {
                if(hasFocus) {
                    resetActionBar();
                    hideKeyboard();
                    v.setVisibility(View.GONE);
                }
            }
        });

        txt_class = (EditText)this.findViewById(R.id.txt_class);
        txt_class.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View v, boolean hasFocus) {
                if (hasFocus) {
                    focusTextBox(v);
                }
            }
        });

        //----------------------------------------------------------------------------------------------------

        txt_school = (AutoCompleteTextView)this.findViewById(R.id.txt_school);

        String[] countries = {"abcd", "efg", "ironman", "whatever", "superman"};
        ArrayAdapter<String> adapter_school = new ArrayAdapter<String>(this, R.layout.acomplete_drop_item_normal,countries);
        txt_school.setAdapter(adapter_school);

        txt_school.setOnFocusChangeListener(new View.OnFocusChangeListener() {
            @Override
            public void onFocusChange(View v, boolean hasFocus) {
                if (hasFocus) {
                    focusTextBox(v);
                }
            }
        });

        //----------------------------------------------------------------------------------------------------
        sp_day = (Spinner)this.findViewById(R.id.sp_day);

        ArrayAdapter<CharSequence> adapter_day = ArrayAdapter.createFromResource(this,
                R.array.date_search_array, R.layout.spinner_item_normal);
        adapter_day.setDropDownViewResource(R.layout.spinner_drop_item_normal);
        sp_day.setAdapter(adapter_day);

        sp_day.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                unfocusTextBoxes();
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

        //------------------------------------------------------------------------------------------
        final ListView lv_schedule = (ListView)this.findViewById(R.id.lv_schedule);
        ScheduleEntry data[] = new ScheduleEntry[]{ new ScheduleEntry("wg", new Date(100000), "11d", (short)42, "subjecT", "teacheR", "new subjecT", "new teacheR", "new rooM", "origiN", "treatmenT", "reasoN"),
                new ScheduleEntry("wg", new Date(System.currentTimeMillis()), "9e", (short)42, "subjecT", "teacheR", "new subjecT", "new teacheR", "new rooM", "origiN", "treatmenT", "reasoN"),
                new ScheduleEntry("wg", new Date(System.currentTimeMillis()), "5a", (short)42, "subjecT", "teacheR", "new subjecT", "new teacheR", "new rooM", "origiN", "treatmenT", "reasoN"),
                new ScheduleEntry("wg", new Date(System.currentTimeMillis()), "6a", (short)12, "subjecT", "teacheR", "new subjecT", "new teacheR", "new rooM", "origiN", "treatmenT", "reasoN")};
        ScheduleAdapter adapter_schedule = new ScheduleAdapter(this, data);
        lv_schedule.setAdapter(adapter_schedule);

        lv_schedule.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                LinearLayout vi = (LinearLayout)view.findViewById(R.id.schedule_row_extra);

                if(vi.getVisibility() == View.VISIBLE) {
                    vi.setVisibility(View.GONE);
/*                    if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
                        vi.setTranslationZ(-30);
                    }*/
                } else {
                    vi.setVisibility(View.VISIBLE);
//                    if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
//                        vi.setTranslationZ(0);
//                    }
                }
            }
        });
    }

    private void unfocusTextBoxes() {
        focus_taker.requestFocus();
    }

    private void hideKeyboard() {
        //hide keyboard
        View view = this.getCurrentFocus();
        if (view != null) {
            InputMethodManager imm = (InputMethodManager)getSystemService(
                    this.INPUT_METHOD_SERVICE);
            imm.hideSoftInputFromWindow(view.getWindowToken(), 0);
        }
    }

    private void resetActionBar() {
        actionBarLayout.setPadding(0,0,0,0);

        this.txt_school.setLayoutParams(paramCollapsed_big);
        this.txt_class.setLayoutParams(paramCollapsed_small);
        this.sp_day.setLayoutParams(paramCollapsed_small);

       if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
            this.txt_school.setTranslationZ(0);
            this.txt_class.setTranslationZ(0);
            this.sp_day.setTranslationZ(0);
        }
    }

    private void focusTextBox(View view) {
        this.resetActionBar();

        int pt = this.pt_to_px(6);
        actionBarLayout.setPadding(pt, pt, pt, pt);

        this.txt_school.setLayoutParams(paramCollapsed_invis);
        this.txt_class.setLayoutParams(paramCollapsed_invis);
        this.sp_day.setLayoutParams(paramCollapsed_invis);

        view.setLayoutParams(paramCollapsed_big);
        if (sdkVersion >= Build.VERSION_CODES.LOLLIPOP) {
            view.setTranslationZ(this.pt_to_px(5));
        }

        focus_taker.setVisibility(View.VISIBLE);
    }

    public int pt_to_px(float dp) {
        float scale = getResources().getDisplayMetrics().density;
        return (int) (dp*scale + 0.5f);
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
