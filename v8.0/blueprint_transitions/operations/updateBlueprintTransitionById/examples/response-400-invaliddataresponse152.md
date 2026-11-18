INVALID_DATA error for an invalid data type in the group_operator field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "group_operator",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].criteria.group[*].group_operator"
      },
      "status": "error"
    }
  ]
}
```
