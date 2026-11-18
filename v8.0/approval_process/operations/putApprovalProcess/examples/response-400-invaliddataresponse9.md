INVALID_DATA error: invalid data given for the rejection_type field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "rejection_type",
        "json_path": "$.approval_process[0].rules[0].rejection_type",
        "supported_values": [
          "all_previous_stages",
          "current_stage",
          "current_approver_decide"
        ]
      },
      "message": "invalid data is given for type",
      "status": "error"
    }
  ]
}
```
