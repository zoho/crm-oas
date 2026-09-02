Error response for missing raw_data_content when body type is raw

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "format",
          "json_path": "$.webhooks[0].body.format"
        },
        "api_name": "raw_data_content",
        "json_path": "$.webhooks[0].body.raw_data_content"
      },
      "message": "raw data content key is mandatory for raw body type",
      "status": "error"
    }
  ]
}
```
