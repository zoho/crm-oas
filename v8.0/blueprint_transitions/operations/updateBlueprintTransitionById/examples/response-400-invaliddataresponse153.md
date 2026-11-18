Error response when the **group_operator** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "group_operator",
        "maximum_length": 3,
        "json_path": "$.transitions[*].criteria.group[*].group_operator"
      },
      "status": "error"
    }
  ]
}
```
