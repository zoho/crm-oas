### `application/json` — Sample

Update a notification channel URL, events, and field-selection conditions

```json
{'channel_id': '1000000068001', 'notify_url': 'https://www.example.com/callback', 'channel_expiry': TimeStamp(2025, 11, 25, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'events': ['Leads.create', 'Contacts.edit', 'Deals.delete'], 'notify_on_related_action': True, 'return_affected_field_values': False, 'notification_condition': [{'type': 'field_selection', 'module': {'api_name': 'Leads'}, 'field_selection': {'group_operator': 'and', 'group': [{'api_name': 'Company'}, {'api_name': 'Email'}]}}], 'token': 'TOKEN_FOR_VERIFICATION_OF_1000000068001'}
```
