DEPENDENT_MISMATCH error when from_address cannot be associated with the to address type

```json
{
  "email_notifications": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "from_address",
          "json_path": "$.email_notifications[0].from_address"
        },
        "api_name": "type",
        "json_path": "$.email_notifications.recipients.to[0].type"
      },
      "message": "from_adress can not be associated for this 'to' address type",
      "status": "error"
    }
  ]
}
```
