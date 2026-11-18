INVALID_DATA error for invalid data in the name field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 6,
        "json_path": "$.transitions[*].during_inputs[*].items[*].name"
      },
      "status": "error"
    }
  ]
}
```
