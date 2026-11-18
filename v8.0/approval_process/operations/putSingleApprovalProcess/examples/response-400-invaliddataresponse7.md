Error response when the approver type has an unsupported value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.approval_process[0].rules[0].approver_stages[7].approver.type",
        "supported_values": [
          "reporting_manager",
          "static",
          "team_users",
          "roles",
          "profiles",
          "groups",
          "users",
          "levels"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
