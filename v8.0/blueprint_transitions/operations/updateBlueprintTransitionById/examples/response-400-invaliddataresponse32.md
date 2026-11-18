The **type** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].type"
      },
      "status": "error"
    }
  ]
}
```
