Error response with code INVALID_DATA: invalid data (field: value)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 1000,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.value"
      },
      "status": "error"
    }
  ]
}
```
