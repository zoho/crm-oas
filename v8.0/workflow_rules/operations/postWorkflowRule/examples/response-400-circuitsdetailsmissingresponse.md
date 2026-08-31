Error response: MANDATORY_NOT_FOUND  - circuits details or circuit_id missing

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "details",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```
