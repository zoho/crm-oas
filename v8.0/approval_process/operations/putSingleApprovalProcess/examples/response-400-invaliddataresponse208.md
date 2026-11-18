INVALID_DATA error when an action layout value is not a JSON object

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
