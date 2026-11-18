INVALID_DATA error: invalid data in the `field` property

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```
