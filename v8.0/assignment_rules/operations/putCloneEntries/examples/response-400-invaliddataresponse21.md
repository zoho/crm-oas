INVALID_DATA error for Assignment Rule data

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
