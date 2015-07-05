package net.batzill.vertretungsplan.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import net.batzill.vertretungsplan.R;
import net.batzill.vertretungsplan.container.ScheduleEntry;

import java.util.Date;

/**
 * Created by Johannes on 05.07.2015.
 */
public class ScheduleAdapter extends BaseAdapter {

    public static String CONVERT_DATE(Context context, Date date) {
        return context.getResources().getStringArray(R.array.day_shortcuts_array)[date.getDay()];
    }


    Context context;
    ScheduleEntry[] data;
    private static LayoutInflater inflater = null;

    public ScheduleAdapter(Context context, ScheduleEntry[] data) {
        this.data = data;
        this.context = context;
        inflater = (LayoutInflater) context
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }

    @Override
    public int getCount() {
        return this.data.length;
    }

    @Override
    public ScheduleEntry getItem(int position) {
        return this.data[position];
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View vi = convertView;
        if (vi == null)
            vi = inflater.inflate(R.layout.schedule_row, null);

        ScheduleEntry entry = this.getItem(position);

        final TextView lbl_day = (TextView)vi.findViewById(R.id.lbl_day);
        lbl_day.setText(CONVERT_DATE(this.context, entry.get_date()));

        final TextView lbl_hour = (TextView)vi.findViewById(R.id.lbl_hour);
        lbl_hour.setText(String.valueOf(entry.get_time()));

        final TextView lbl_teacher = (TextView)vi.findViewById(R.id.lbl_teacher);
        lbl_teacher.setText(entry.get_teacher());

        final TextView lbl_subject = (TextView)vi.findViewById(R.id.lbl_subject);
        lbl_subject.setText(entry.get_subject());

        final TextView lbl_new_subject = (TextView)vi.findViewById(R.id.lbl_new_subject);
        lbl_new_subject.setText(entry.get_new_room());

        final TextView lbl_new_room = (TextView)vi.findViewById(R.id.lbl_new_room);
        lbl_new_room.setText(entry.get_new_room());

        final TextView lbl_new_teacher = (TextView)vi.findViewById(R.id.lbl_new_teacher);
        lbl_new_teacher.setText(entry.get_new_teacher());

        final TextView lbl_origin = (TextView)vi.findViewById(R.id.lbl_origin);
        lbl_origin.setText(entry.get_origin());

        final TextView lbl_treatment = (TextView)vi.findViewById(R.id.lbl_treatment);
        lbl_treatment.setText(entry.get_treatment());


        return vi;
    }
}
