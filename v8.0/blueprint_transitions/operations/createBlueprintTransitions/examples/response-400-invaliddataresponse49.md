Error response with code **INVALID_DATA**: **validation_message** exceeds the maximum length of 39

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "validation_message",
        "maximum_length": 39,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.validation_message"
      },
      "status": "error"
    }
  ]
}
```
