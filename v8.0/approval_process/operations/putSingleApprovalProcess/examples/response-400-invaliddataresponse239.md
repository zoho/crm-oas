Invalid value on **rejection_type** outside the supported values

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rejection_type",
        "supported_values": [
          "all_previous_stages",
          "current_stage",
          "current_approver_decide"
        ],
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.rejection_type"
      },
      "status": "error"
    }
  ]
}
```
