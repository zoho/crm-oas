The **optional** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "optional",
        "maximum_length": 5,
        "json_path": "$.transitions[*].during_inputs[*].optional"
      },
      "status": "error"
    }
  ]
}
```
