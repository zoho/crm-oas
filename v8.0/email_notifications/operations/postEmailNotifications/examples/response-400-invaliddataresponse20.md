INVALID_DATA error — type field value exceeds maximum length

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
