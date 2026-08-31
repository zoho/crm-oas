### `application/json` — Sample

Replace all details of a notification channel

```json
{'watch': [{'channel_id': '1000000068001', 'notify_url': 'https://www.example.com/callback', 'channel_expiry': TimeStamp(2025, 11, 25, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'events': ['Leads.create', 'Contacts.edit', 'Deals.delete'], 'notification_condition': [{'type': 'field_selection'}], 'notify_on_related_action': True, 'token': 'TOKEN_FOR_VERIFICATION_OF_1000000068001'}]}
```
