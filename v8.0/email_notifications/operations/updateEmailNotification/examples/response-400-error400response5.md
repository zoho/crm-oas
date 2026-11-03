INVALID_DATA error — id field value exceeds maximum length

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.email_notifications[*].from_address.resource.id"
    },
    "status": "error"
  }
}
```
