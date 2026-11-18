Missing criteria error for an approval rule

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "criteria",
        "json_path": "$.approval_process[*].rules[*].criteria"
      },
      "status": "error"
    }
  ]
}
```
