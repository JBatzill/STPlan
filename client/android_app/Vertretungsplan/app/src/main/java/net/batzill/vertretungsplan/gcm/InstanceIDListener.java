package net.batzill.vertretungsplan.gcm;

import android.content.Intent;

import com.google.android.gms.iid.InstanceID;
import com.google.android.gms.iid.InstanceIDListenerService;

/**
 * Created by Johannes on 7/11/2015.
 */
public class InstanceIDListener extends InstanceIDListenerService {
    public void onTokenRefresh() {
        // Fetch updated Instance ID token and notify our app's server of any changes (if applicable).
        //Intent intent = new Intent(this, RegistrationIntentService.class);
        //startService(intent);
    }
}