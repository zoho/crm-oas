INVALID_DATA when approver type is not a supported value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "users",
          "levels",
          "roles",
          "groups",
          "static",
          "reporting_manager",
          "profiles",
          "team_users"
        ],
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.type"
      },
      "status": "error"
    }
  ]
}
```
