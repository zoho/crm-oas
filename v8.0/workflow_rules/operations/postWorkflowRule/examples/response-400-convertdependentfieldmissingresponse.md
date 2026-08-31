Error response: DEPENDENT_FIELD_MISSING  - convert action missing mandatory fields for Leads

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "add_to_existing_contact",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.add_to_existing_contact"
      },
      "message": "Required dependent field is missing",
      "status": "error"
    }
  ]
}
```
