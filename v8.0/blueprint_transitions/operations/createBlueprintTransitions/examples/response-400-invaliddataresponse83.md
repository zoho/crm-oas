Error response with code **INVALID_DATA**: the **optional** field exceeds the maximum length of 5

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "optional",
        "maximum_length": 5,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].optional"
      },
      "status": "error"
    }
  ]
}
```
