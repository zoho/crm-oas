INVALID_DATA error when field_mappings is not of type jsonarray

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
