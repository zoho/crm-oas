INVALID_DATA error: the actions field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].actions"
      },
      "status": "error"
    }
  ]
}
```
