Error response with code **INVALID_DATA** for invalid data in the **optional** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "optional",
        "maximum_length": 5,
        "json_path": "$.transitions[*].during_inputs[*].optional"
      },
      "status": "error"
    }
  ]
}
```
