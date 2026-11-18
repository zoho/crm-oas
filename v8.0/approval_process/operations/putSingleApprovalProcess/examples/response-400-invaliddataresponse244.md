INVALID_DATA error when the actions key is not a JSON array

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions"
      },
      "status": "error"
    }
  ]
}
```
