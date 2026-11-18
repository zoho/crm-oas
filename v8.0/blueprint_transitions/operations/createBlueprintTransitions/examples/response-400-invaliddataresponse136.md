Error response with code **INVALID_DATA**: invalid data type for the **name** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "null",
        "json_path": "$.transitions[*].actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
