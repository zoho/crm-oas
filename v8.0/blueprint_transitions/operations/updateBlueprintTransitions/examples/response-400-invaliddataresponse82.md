Error response with code INVALID_DATA: Invalid data (Field: comparator)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "comparator",
        "maximum_length": 50,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
