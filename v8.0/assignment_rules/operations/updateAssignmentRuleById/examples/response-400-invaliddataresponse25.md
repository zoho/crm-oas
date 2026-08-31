INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "tasks"
        ],
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
