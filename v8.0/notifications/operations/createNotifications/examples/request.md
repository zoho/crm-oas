### `application/json` — Sample

Create two notification channels with event subscriptions

```json
{'watch': [{'channel_id': '1000000068001', 'notify_url': 'https://www.example.com/notify', 'events': ['Leads.create', 'Contacts.edit'], 'channel_expiry': TimeStamp(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'token': 'TOKEN_FOR_VERIFICATION_1'}, {'channel_id': '1000000068002', 'notify_url': 'https://www.example.com/notify2', 'events': ['Deals.delete'], 'channel_expiry': TimeStamp(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'token': 'TOKEN_FOR_VERIFICATION_2'}]}
```
