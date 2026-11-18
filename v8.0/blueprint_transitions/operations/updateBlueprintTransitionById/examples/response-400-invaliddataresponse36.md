**INVALID_DATA** error: the **sequence** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence",
        "expected_data_type": "integer",
        "json_path": "$.transitions[*].during_inputs[*].sequence"
      },
      "status": "error"
    }
  ]
}
```
