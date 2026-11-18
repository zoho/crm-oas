Error response with code INVALID_DATA: Invalid data (Field: validation_message)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "validation_message",
        "maximum_length": 1000,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
