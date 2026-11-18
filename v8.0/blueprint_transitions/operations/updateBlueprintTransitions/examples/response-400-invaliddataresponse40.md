Error response with code INVALID_DATA: Invalid data (Field: sequence)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "sequence",
        "maximum_length": 100,
        "json_path": "$.transitions[*].during_inputs[*].sequence"
      },
      "status": "error"
    }
  ]
}
```
