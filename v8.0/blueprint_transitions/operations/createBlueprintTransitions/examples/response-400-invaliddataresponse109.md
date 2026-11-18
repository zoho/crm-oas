Error response with code **INVALID_DATA** due to invalid data in the **optional** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "optional",
        "maximum_length": 4,
        "json_path": "$.transitions[*].during_inputs[*].items[*].optional"
      },
      "status": "error"
    }
  ]
}
```
