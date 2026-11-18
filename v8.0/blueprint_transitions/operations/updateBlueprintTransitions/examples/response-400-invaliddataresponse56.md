Error response with code INVALID_DATA: Invalid data (Field: field)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.field"
      },
      "status": "error"
    }
  ]
}
```
