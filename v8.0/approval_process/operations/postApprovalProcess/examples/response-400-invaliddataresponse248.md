Invalid data type error on the ID field of the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.layout.id"
      },
      "status": "error"
    }
  ]
}
```
