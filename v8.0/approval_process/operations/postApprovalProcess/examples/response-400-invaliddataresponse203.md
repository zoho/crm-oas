Invalid data type error naming the field **ID**

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout.id"
      },
      "status": "error"
    }
  ]
}
```
