INVALID_DATA error for an invalid data type in the actions field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions"
      },
      "status": "error"
    }
  ]
}
```
