MANDATORY_NOT_FOUND error: required field_mappings missing

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
