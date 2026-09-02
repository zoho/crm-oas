Field value has an incorrect data type for webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```
