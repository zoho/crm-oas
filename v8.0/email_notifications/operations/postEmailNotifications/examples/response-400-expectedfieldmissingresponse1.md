EXPECTED_FIELD_MISSING error — module id or api_name not specified

```json
{
  "email_notifications": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.email_notifications[0].module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.email_notifications[0].module.api_name"
          }
        ]
      },
      "message": "Specify At least one field",
      "status": "error"
    }
  ]
}
```
