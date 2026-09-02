Error response with code INVALID_DATA: Invalid data type (Field: sequence_number)

```json
{
  "assignment_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence_number",
        "expected_data_type": "integer",
        "json_path": "$.assignment_rules[0].rule_entries[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```
