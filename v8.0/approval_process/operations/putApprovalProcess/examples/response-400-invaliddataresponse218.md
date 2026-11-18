Error response with code INVALID_DATA: Invalid data type (Field: api_name)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
