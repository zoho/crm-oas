INVALID_DATA error when the **name** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "null",
        "json_path": "$.transitions[*].actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
