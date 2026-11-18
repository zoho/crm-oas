INVALID_DATA error for an invalid data type on the resource field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "resource",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource"
      },
      "status": "error"
    }
  ]
}
```
