Error response with code INVALID_DATA for invalid data in the name field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 10,
        "json_path": "$.transitions[*].during_inputs[*].kiosk.name"
      },
      "status": "error"
    }
  ]
}
```
