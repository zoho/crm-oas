Error response with code **INVALID_DATA** for an invalid data type in the **optional** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "optional",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].optional"
      },
      "status": "error"
    }
  ]
}
```
