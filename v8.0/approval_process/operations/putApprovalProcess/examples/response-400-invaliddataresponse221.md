Error response with code INVALID_DATA: Invalid data (Field: field_mappings)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field_mappings",
        "maximum_length": 500,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings"
      },
      "status": "error"
    }
  ]
}
```
