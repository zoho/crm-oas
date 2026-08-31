Error response

```json
{
  "assignment_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.assignment_rules[*].default_assignee.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.assignment_rules[*].default_assignee.assignment_rules.default_assignee.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
