Invalid data type error on the name field with expected text format

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
