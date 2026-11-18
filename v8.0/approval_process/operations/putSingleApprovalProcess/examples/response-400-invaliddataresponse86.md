INVALID_DATA error when approval_order has an invalid data type

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
