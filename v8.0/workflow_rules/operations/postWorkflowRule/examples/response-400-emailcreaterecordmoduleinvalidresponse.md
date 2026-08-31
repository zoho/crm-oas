Error response: INVALID_DATA  - create_record_email module must be Leads or Contacts

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
