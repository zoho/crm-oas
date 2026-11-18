Error response with code **INVALID_DATA**: **validation_filter** exceeds the maximum length of 1

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "validation_filter",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter"
      },
      "status": "error"
    }
  ]
}
```
