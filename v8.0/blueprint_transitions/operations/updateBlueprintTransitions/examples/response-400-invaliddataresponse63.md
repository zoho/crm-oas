Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "bigint",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.value"
      },
      "status": "error"
    }
  ]
}
```
