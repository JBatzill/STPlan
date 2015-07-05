package net.batzill.vertretungsplan.container;

import java.util.Date;
import java.util.Dictionary;
import java.util.Map;

/**
 * Created by Johannes on 05.07.2015.
 */
public class ScheduleEntry {
    private String __school = "";
    private Date __date = new Date(1993, 1, 23);
    private String __class = "";
    private short __time = 1;
    private String __subject = "";
    private String __teacher = "";
    private String __new_subject = "";
    private String __new_teacher = "";
    private String __new_room = "";
    private String __origin = "";
    private String __treatment = "";
    private String __reason = "";

    public ScheduleEntry(String school, Date date, String _class, short time, String subject, String teacher, String new_subject, String new_teacher, String new_room, String origin, String treatment, String reason) {
        this.__school = school;
        this.__date = date;
        this.__class = _class;
        this.__time = time;
        this.__subject = subject;
        this.__teacher = teacher;
        this.__new_subject = new_subject;
        this.__new_teacher = new_teacher;
        this.__new_room = new_room;
        this.__origin = origin;
        this.__treatment = treatment;
        this.__reason = reason;
    }

    public ScheduleEntry(Map<String, String> dic) {
        this.__school = dic.containsKey("_school") ? dic.get("_school") : __school;
        this.__date = dic.containsKey("_date") ? new Date(dic.get("_date")) : __date;
        this.__class = dic.containsKey("_class") ? dic.get("_class") : __class;
        this.__time = dic.containsKey("_time") ? Short.valueOf(dic.get("_time")) : __time;
        this.__subject = dic.containsKey("_subject") ? dic.get("_subject") : __subject;
        this.__teacher = dic.containsKey("_teacher") ? dic.get("_teacher") : __teacher;
        this.__new_subject = dic.containsKey("_new_subject") ? dic.get("_new_subject") : __new_subject;
        this.__new_teacher = dic.containsKey("_new_teacher") ? dic.get("_new_teacher") : __new_teacher;
        this.__new_room = dic.containsKey("_new_room") ? dic.get("_new_room") : __new_room;
        this.__origin = dic.containsKey("_origin") ? dic.get("_origin") : __origin;
        this.__treatment = dic.containsKey("_treatment") ? dic.get("_treatment") : __treatment;
        this.__reason = dic.containsKey("_reason") ? dic.get("_reason") : __reason;
    }

    public String get_school() {
        return __school;
    }
    public Date get_date() {
        return __date;
    }
    public String get_class() {
        return __class;
    }
    public Short get_time() {
        return __time;
    }
    public String get_subject() {
        return __subject;
    }
    public String get_teacher() {
        return __teacher;
    }
    public String get_new_subject() {
        return __new_subject;
    }
    public String get_new_teacher() {
        return __new_teacher;
    }
    public String get_new_room() {
        return __new_room;
    }
    public String get_origin() {
        return __origin;
    }
    public String get_treatment() {
        return __treatment;
    }
    public String get_reason() {
        return __reason;
    }
}
