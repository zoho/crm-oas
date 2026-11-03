INVALID_DATA error for invalid data type in template field

```json
{
  "email_notifications": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "template",
        "expected_data_type": "jsonobject",
        "json_path": "$.email_notifications[*].template"
      },
      "status": "error"
    }
  ]
}
```
