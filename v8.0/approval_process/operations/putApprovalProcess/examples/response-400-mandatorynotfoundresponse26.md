MANDATORY_NOT_FOUND error: during_approval_waiting policy missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "during_approval_waiting",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting"
      },
      "status": "error"
    }
  ]
}
```
