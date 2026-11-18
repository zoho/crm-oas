Error response with code INVALID_DATA: Invalid data type (Field: field_mappings)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field_mappings",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings"
      },
      "status": "error"
    }
  ]
}
```
