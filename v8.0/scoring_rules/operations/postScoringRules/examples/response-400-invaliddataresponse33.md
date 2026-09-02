Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.scoring_rules[0].signal_rules[0].signal.id"
      },
      "status": "error"
    }
  ]
}
```
