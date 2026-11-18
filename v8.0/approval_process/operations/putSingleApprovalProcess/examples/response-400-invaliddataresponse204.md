Error when an action name is not a text value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
