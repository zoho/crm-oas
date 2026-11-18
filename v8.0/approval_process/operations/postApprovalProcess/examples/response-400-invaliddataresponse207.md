INVALID_DATA error for an invalid module data type in the request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module"
      },
      "status": "error"
    }
  ]
}
```
