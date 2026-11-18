Error response with code **INVALID_DATA**: the **optional** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "optional",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].optional"
      },
      "status": "error"
    }
  ]
}
```
