Error response with code **INVALID_DATA**: the **value** field exceeds the maximum length of 4

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 4,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.value"
      },
      "status": "error"
    }
  ]
}
```
