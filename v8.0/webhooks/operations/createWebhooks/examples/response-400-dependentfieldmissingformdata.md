Error response for missing form_data_content when type is form_data

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.webhooks[0].body.type"
        },
        "api_name": "form_data_content",
        "json_path": "$.webhooks[0].body.form_data_content"
      },
      "message": "form data content key is mandatory for form body type",
      "status": "error"
    }
  ]
}
```
