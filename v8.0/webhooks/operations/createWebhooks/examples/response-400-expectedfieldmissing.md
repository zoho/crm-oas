Error response when module is missing both ID and api_name.

```json
{
  "webhooks": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.webhooks[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.webhooks[0].module.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
