INVALID_DATA error: wrong data type for the approval_order field

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
