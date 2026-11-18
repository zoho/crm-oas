Invalid data error for field_mappings exceeding 500 entries after rejection

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_mappings",
        "maximum_length": 500,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings"
      },
      "status": "error"
    }
  ]
}
```
