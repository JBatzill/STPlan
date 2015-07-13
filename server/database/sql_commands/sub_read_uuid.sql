SELECT 'subscription'._id, 'subscription'._school_id, 'subscription'._class FROM
'subscription', (SELECT 'user'._id FROM 'user' WHERE _uuid = :_uuid)
ON 'subscription'._user_id = 'user'._id;