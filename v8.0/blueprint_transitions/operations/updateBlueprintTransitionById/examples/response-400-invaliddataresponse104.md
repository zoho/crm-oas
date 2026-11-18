INVALID_DATA error for an invalid data type in the items field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "items",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].during_inputs[*].items"
      },
      "status": "error"
    }
  ]
}
```
