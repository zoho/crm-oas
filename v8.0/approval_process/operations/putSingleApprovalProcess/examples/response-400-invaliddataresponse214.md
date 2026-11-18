Invalid data type error for the module object in a final approval action

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
