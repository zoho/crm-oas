INVALID_DATA error when current_record_module ID exceeds the maximum allowed length

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.kiosks[*].current_record_module.id"
      },
      "status": "error"
    }
  ]
}
```
