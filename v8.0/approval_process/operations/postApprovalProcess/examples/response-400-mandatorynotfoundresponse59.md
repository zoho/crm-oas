MANDATORY_NOT_FOUND error for a missing **field_mappings** field after rejection

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field_mappings",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings"
      },
      "status": "error"
    }
  ]
}
```
