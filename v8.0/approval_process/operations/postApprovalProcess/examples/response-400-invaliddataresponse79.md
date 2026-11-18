INVALID_DATA error for an invalid data type in the approval_order field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "approval_order",
        "expected_data_type": "integer",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].approval_order"
      },
      "status": "error"
    }
  ]
}
```
