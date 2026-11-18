INVALID_DATA error for invalid data type in the field property

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings[*].field"
      },
      "status": "error"
    }
  ]
}
```
