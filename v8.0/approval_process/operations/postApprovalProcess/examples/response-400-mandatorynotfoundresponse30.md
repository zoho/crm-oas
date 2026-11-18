MANDATORY_NOT_FOUND error for the missing ID field in the create request

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource.id"
      },
      "status": "error"
    }
  ]
}
```
