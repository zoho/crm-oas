Invalid data type error naming the field **field**

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field"
      },
      "status": "error"
    }
  ]
}
```
