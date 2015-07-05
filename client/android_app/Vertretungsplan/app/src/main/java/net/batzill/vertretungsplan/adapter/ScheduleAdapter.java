package net.batzill.vertretungsplan.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

import net.batzill.vertretungsplan.R;
import net.batzill.vertretungsplan.container.ScheduleEntry;

/**
 * Created by Johannes on 05.07.2015.
 */
public class ScheduleAdapter extends BaseAdapter {

    Context context;
    ScheduleEntry[] data;
    private static LayoutInflater inflater = null;

    public ScheduleAdapter(Context context, ScheduleEntry[] data) {
        this.context = context;
        this.data = data;
        inflater = (LayoutInflater) context
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }

    @Override
    public int getCount() {
        return data.length;
    }

    @Override
    public Object getItem(int position) {
        return data[position];
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


        return vi;
    }
}
