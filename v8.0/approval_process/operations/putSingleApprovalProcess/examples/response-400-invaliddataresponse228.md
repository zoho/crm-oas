INVALID_DATA error: wrong data type for the field mapping type field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```
