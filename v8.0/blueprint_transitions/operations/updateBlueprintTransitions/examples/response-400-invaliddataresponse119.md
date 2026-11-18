Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.transitions[*].during_inputs[*].kiosk.name"
      },
      "status": "error"
    }
  ]
}
```
