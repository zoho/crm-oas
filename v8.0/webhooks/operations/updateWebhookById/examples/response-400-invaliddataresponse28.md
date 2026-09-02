Field value has an incorrect data type in webhook configuration

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "url",
        "expected_data_type": "website",
        "json_path": "$.webhooks[*].url"
      },
      "status": "error"
    }
  ]
}
```
