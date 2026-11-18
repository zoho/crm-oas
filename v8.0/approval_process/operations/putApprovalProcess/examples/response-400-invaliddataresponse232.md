INVALID_DATA error: field mapping value exceeds maximum length of 4

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 4,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings[*].value"
      },
      "status": "error"
    }
  ]
}
```
