Error response when the **trigger_type** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "trigger_type",
        "maximum_length": 100,
        "json_path": "$.transitions[*].trigger_type"
      },
      "status": "error"
    }
  ]
}
```
