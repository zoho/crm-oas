**INVALID_DATA** error when **trigger_type** has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "trigger_type",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].trigger_type"
      },
      "status": "error"
    }
  ]
}
```
