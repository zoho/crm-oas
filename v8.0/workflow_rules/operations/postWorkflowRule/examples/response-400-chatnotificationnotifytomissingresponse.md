Error response: DEPENDENT_FIELD_MISSING  - notify_to id/name missing for user/channel type

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.id"
      },
      "message": "Required dependent field is missing",
      "status": "error"
    }
  ]
}
```
