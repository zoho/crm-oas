Error response with code INVALID_DATA: Invalid data type (Field: sequence)

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
