INVALID_DATA error when notify_original_approvers_via exceeds maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
