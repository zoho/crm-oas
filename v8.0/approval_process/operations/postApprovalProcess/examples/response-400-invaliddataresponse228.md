Invalid data type error for the actions_upon_rejection field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions_upon_rejection",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection"
      },
      "status": "error"
    }
  ]
}
```
