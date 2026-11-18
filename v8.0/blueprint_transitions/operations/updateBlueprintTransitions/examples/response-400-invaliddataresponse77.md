Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
