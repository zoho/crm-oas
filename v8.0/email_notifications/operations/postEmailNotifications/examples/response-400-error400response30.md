INVALID_DATA error for unsupported value in the recipient type field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "merge_field",
        "group",
        "role",
        "role_and_subordinate",
        "territory",
        "territory_and_subterritory",
        "emails",
        "user",
        "profile"
      ],
      "json_path": "$.email_notifications[*].reply_to_address.type"
    },
    "status": "error"
  }
}
```
