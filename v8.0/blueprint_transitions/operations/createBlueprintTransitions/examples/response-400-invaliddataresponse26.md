Error response with code **INVALID_DATA**: invalid data type in the **api_name** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```
