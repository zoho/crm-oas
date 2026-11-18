Invalid data in an optional field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "optional",
        "maximum_length": 4,
        "json_path": "$.transitions[*].during_inputs[*].items[*].optional"
      },
      "status": "error"
    }
  ]
}
```
