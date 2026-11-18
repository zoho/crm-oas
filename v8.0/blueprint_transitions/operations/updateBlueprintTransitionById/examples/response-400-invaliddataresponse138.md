INVALID_DATA error when the **owners** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "owners",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].owners"
      },
      "status": "error"
    }
  ]
}
```
