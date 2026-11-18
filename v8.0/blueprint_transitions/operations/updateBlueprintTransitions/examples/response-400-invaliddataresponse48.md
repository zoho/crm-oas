Error response with code INVALID_DATA: Invalid data (Field: message)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "message",
        "maximum_length": 1000,
        "json_path": "$.transitions[*].during_inputs[*].message"
      },
      "status": "error"
    }
  ]
}
```
