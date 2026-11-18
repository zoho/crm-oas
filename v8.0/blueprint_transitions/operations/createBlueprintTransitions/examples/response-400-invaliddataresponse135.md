Error response with code **INVALID_DATA**: invalid data type for the **overwrite** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "overwrite",
        "expected_data_type": "boolean",
        "json_path": "$.transitions[*].actions[*].details.overwrite"
      },
      "status": "error"
    }
  ]
}
```
