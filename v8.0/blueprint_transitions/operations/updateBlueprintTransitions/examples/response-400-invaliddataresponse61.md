Error response with code INVALID_DATA: Invalid data type (Field: comparator)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "comparator",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
