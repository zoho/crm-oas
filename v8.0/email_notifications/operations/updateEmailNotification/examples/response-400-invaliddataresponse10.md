INVALID_DATA error response for invalid data on the recipients field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "recipients",
        "maximum_length": 1,
        "json_path": "$.email_notifications[*].recipients"
      },
      "status": "error"
    }
  ]
}
```
