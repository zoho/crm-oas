INVALID_DATA error for invalid data in reply_to_address field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "reply_to_address",
        "maximum_length": 2,
        "json_path": "$.email_notifications[*].reply_to_address"
      },
      "status": "error"
    }
  ]
}
```
