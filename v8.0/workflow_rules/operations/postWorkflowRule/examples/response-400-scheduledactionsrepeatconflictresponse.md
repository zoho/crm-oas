Error response with code DEPENDENT_MISMATCH: scheduled_actions not supported with repeat=true

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "repeat",
          "json_path": "$.workflow_rules[0].execute_when.details.repeat"
        },
        "api_name": "scheduled_actions",
        "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```
