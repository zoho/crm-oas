400 MANDATORY_NOT_FOUND when the required overall_approval_type field is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "overall_approval_type",
        "json_path": "$.approval_process[*].rules[*].overall_approval_type"
      },
      "status": "error"
    }
  ]
}
```
