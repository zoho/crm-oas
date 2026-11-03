INVALID_DATA error response for unsupported value on the type field

```json
{
  "email_notifications": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "merge_field",
        "email",
        "user",
        "organization_email"
      ],
      "json_path": "$.email_notifications[*].from_address.type"
    },
    "status": "error"
  }
}
```
