package net.batzill.vertretungsplan.gcm;

import android.app.IntentService;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import com.google.android.gms.gcm.GcmListenerService;
import com.google.android.gms.gcm.GoogleCloudMessaging;

import java.util.logging.Handler;

/**
 * Created by Johannes on 7/11/2015.
 */
public class GcmMessageHandler extends GcmListenerService {

    public GcmMessageHandler() {
        super();
    }

    @Override
    public void onDeletedMessages() {
        //msgs on server got deleted
    }

    @Override
    public void onMessageReceived(String from, Bundle data) {
        int a = 3;
    }
}