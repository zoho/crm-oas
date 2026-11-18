Error response with code **INVALID_DATA**: invalid data type in **details**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
