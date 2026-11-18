MANDATORY_NOT_FOUND error when the required sequence_number field is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "sequence_number",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```
