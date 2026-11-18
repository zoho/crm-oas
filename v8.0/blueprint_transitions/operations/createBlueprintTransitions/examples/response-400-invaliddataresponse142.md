**INVALID_DATA** error: invalid data type in the **resources** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resources",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].owners[*].resources"
      },
      "status": "error"
    }
  ]
}
```
