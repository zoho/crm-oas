Field value has an incorrect data type in a webhook property

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].name"
      },
      "status": "error"
    }
  ]
}
```
