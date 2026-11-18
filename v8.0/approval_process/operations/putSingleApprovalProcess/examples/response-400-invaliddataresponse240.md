Invalid data type error on the **notify_original_approvers_via** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "notify_original_approvers_via",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.notify_original_approvers_via"
      },
      "status": "error"
    }
  ]
}
```
