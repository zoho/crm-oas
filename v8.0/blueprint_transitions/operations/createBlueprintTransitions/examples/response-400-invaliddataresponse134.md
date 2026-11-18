Error response with code **INVALID_DATA**: invalid data for the **color** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "color",
        "maximum_length": 100,
        "json_path": "$.transitions[*].actions[*].details.tags[*].color"
      },
      "status": "error"
    }
  ]
}
```
