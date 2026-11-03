INVALID_DATA error for invalid data length on type field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 11,
        "json_path": "$.email_notifications[*].recipients.to[*].type"
      },
      "status": "error"
    }
  ]
}
```
