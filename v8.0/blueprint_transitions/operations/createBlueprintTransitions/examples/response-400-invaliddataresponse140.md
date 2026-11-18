**INVALID_DATA** error: invalid data type in the **type** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].owners[*].type"
      },
      "status": "error"
    }
  ]
}
```
