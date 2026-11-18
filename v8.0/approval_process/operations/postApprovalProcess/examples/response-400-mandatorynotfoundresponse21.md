MANDATORY_NOT_FOUND error for the missing approval_order field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "approval_order",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].approval_order"
      },
      "status": "error"
    }
  ]
}
```
