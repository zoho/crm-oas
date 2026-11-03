INVALID_DATA error for invalid resource field value

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "resource",
      "maximum_length": 1,
      "json_path": "$.email_notifications[*].from_address.resource"
    },
    "status": "error"
  }
}
```
