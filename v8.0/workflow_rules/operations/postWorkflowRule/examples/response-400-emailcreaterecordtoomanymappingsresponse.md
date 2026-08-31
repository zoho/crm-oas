Error response: LIMIT_EXCEEDED  - create_record_email allows exactly 1 field_mapping

```json
{
  "workflow_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "field_mappings",
        "limit": 1,
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.field_mappings"
      },
      "message": "too many records",
      "status": "error"
    }
  ]
}
```
