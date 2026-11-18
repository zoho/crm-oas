Error response with code **INVALID_DATA**: invalid data type for the **color** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "color",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].actions[*].details.tags[*].color"
      },
      "status": "error"
    }
  ]
}
```
