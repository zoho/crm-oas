INVALID_DATA error when the actions key is not a JSON object

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions"
      },
      "status": "error"
    }
  ]
}
```
