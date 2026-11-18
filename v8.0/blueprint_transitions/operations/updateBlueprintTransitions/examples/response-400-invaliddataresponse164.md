Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.transitions[*].criteria.group[*].group[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
