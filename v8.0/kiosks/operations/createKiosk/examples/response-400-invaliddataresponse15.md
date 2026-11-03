INVALID_DATA error when current_record_module api_name is not a text type

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.kiosks[*].current_record_module.api_name"
      },
      "status": "error"
    }
  ]
}
```
