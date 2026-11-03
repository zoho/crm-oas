INVALID_DATA error for invalid from_address value

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "from_address",
        "maximum_length": 2,
        "json_path": "$.email_notifications[*].from_address"
      },
      "status": "error"
    }
  ]
}
```
