**INVALID_DATA** error when **api_name** is invalid

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 14,
        "json_path": "$.transitions[*].criteria.group[*].group[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
