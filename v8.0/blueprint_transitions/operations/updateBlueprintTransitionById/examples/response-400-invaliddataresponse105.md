INVALID_DATA error for invalid data in the items field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "items",
        "maximum_length": 2,
        "json_path": "$.transitions[*].during_inputs[*].items"
      },
      "status": "error"
    }
  ]
}
```
