Error response with code **INVALID_DATA**: Invalid data (Field: **name**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 7,
        "json_path": "$.transitions[*].actions[*].details.tags[*].name"
      },
      "status": "error"
    }
  ]
}
```
