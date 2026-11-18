**MANDATORY_NOT_FOUND** error when the action **id** is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
