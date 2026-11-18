Error response with code INVALID_DATA: Invalid data (Field: optional)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "optional",
        "maximum_length": 100,
        "json_path": "$.transitions[*].during_inputs[*].items[*].optional"
      },
      "status": "error"
    }
  ]
}
```
