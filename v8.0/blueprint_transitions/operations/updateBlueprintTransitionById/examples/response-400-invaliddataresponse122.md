INVALID_DATA: invalid data in the **details** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 1,
        "json_path": "$.transitions[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
