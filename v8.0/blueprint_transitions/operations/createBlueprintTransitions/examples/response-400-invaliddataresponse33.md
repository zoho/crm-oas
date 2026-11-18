Error response with code **INVALID_DATA** for invalid data in the **type** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 4,
        "json_path": "$.transitions[*].during_inputs[*].type"
      },
      "status": "error"
    }
  ]
}
```
