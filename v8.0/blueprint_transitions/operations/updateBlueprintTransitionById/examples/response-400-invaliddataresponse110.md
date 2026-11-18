Invalid data type for the sequence field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence",
        "expected_data_type": "integer",
        "json_path": "$.transitions[*].during_inputs[*].items[*].sequence"
      },
      "status": "error"
    }
  ]
}
```
