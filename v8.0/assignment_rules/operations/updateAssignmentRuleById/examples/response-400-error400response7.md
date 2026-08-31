Error response

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "users",
          "role",
          "group",
          "profile",
          "criteria",
          "zia_suggested_users"
        ],
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
      },
      "status": "error"
    }
  ]
}
```
