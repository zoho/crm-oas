INVALID_DATA error: invalid data in the type field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "type",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.type",
        "supported_values": [
          "users",
          "roles",
          "groups",
          "levels",
          "reporting_manager",
          "static",
          "team_users",
          "profiles"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
