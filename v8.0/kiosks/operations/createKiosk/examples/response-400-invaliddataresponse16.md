INVALID_DATA error when current_record_module api_name exceeds the maximum allowed length

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 250,
        "json_path": "$.kiosks[*].current_record_module.api_name"
      },
      "status": "error"
    }
  ]
}
```
