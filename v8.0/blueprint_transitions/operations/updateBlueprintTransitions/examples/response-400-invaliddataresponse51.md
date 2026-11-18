Error response with code INVALID_DATA: Invalid data type (Field: validation_message)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "validation_message",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
