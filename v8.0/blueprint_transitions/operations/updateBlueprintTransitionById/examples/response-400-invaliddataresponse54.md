Invalid data type for the api_name field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
