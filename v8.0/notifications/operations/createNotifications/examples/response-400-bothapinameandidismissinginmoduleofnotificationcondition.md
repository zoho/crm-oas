Both api_name and module ID missing from the notification condition

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify atleast one field",
  "details": {
    "expected_fields": [
      {
        "api_name": "api_name",
        "json_path": "$.watch[0].notification_condition[0].module.api_name"
      },
      {
        "api_name": "id",
        "json_path": "$.watch[0].notification_condition[0].module.id"
      }
    ]
  },
  "status": "error"
}
```
