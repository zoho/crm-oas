Error response when the **value** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 1000,
        "json_path": "$.transitions[*].criteria.group[*].group[*].value"
      },
      "status": "error"
    }
  ]
}
```
