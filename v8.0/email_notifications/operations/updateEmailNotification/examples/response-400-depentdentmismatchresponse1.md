DEPENDENT_MISMATCH error when reply_to_address is incompatible with the selected from_address type

```json
{
  "email_notifications": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "from_address",
          "json_path": "$.email_notifications[0].reply_to_address"
        },
        "api_name": "type",
        "json_path": "$.email_notifications.recipients.to[0].type"
      },
      "message": "reply_to_adress can not be associated for this 'to' address type",
      "status": "error"
    }
  ]
}
```
