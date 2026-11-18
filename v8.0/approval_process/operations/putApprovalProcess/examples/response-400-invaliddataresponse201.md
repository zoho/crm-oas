Error response with code INVALID_DATA: Invalid data type (Field: type)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
