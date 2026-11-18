INVALID_DATA invalid data type for field 'layout' in approval process update

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layout",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout"
      },
      "status": "error"
    }
  ]
}
```
