Error response when the **group** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "group",
        "maximum_length": 2,
        "json_path": "$.transitions[*].criteria.group[*].group"
      },
      "status": "error"
    }
  ]
}
```
