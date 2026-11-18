MANDATORY_NOT_FOUND error for the missing rule name field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.approval_process[*].rules[*].name"
      },
      "status": "error"
    }
  ]
}
```
