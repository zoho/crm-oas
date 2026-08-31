INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "user_availability_based_on",
        "supported_values": [
          "online_status",
          "shift_timing"
        ],
        "json_path": "$.assignment_rules[*].rule_entries[*].user_availability_based_on"
      },
      "status": "error"
    }
  ]
}
```
