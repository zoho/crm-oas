INVALID_DATA error for an invalid data type in the group field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "group",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].criteria.group"
      },
      "status": "error"
    }
  ]
}
```
