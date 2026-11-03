INVALID_DATA error for invalid reply_to_address value

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "reply_to_address",
        "maximum_length": 100,
        "json_path": "$.email_notifications[*].reply_to_address"
      },
      "status": "error"
    }
  ]
}
```
