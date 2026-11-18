**INVALID_DATA** error when a **field** value is invalid

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.transitions[*].criteria.group[*].group[*].field"
      },
      "status": "error"
    }
  ]
}
```
