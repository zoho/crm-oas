Error response with code **INVALID_DATA**: **validation_filter** has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "validation_filter",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter"
      },
      "status": "error"
    }
  ]
}
```
