Error response with code **INVALID_DATA**: invalid data (field: **api_name**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 8,
        "json_path": "$.transitions[*].actions[*].details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
