INVALID_DATA error when current_record_module ID is not a bigint type

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.kiosks[*].current_record_module.id"
      },
      "status": "error"
    }
  ]
}
```
