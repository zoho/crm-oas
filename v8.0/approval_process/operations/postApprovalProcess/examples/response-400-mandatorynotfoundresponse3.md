MANDATORY_NOT_FOUND error for a missing rule name in the create request

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.approval_process[0].rules[0].name"
      },
      "message": "The rule name is missing",
      "status": "error"
    }
  ]
}
```
