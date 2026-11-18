Invalid data error for the notify_original_approvers_via field without a type detail

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "notify_original_approvers_via",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.notify_original_approvers_via"
      },
      "status": "error"
    }
  ]
}
```
