INVALID_DATA when notify_original_approvers_via under rejection actions exceeds max length 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "notify_original_approvers_via",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.notify_original_approvers_via"
      },
      "status": "error"
    }
  ]
}
```
