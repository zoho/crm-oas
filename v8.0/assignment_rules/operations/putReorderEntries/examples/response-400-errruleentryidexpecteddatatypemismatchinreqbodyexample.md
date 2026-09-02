Error response with code INVALID_DATA: Invalid data type (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.assignment_rules[0].rule_entries[*].id"
      },
      "status": "error"
    }
  ]
}
```
