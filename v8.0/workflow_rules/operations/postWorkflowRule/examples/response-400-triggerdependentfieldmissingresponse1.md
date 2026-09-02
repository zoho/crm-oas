Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: repeat)

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.workflow_rules[0].execute_when.type"
        },
        "api_name": "repeat",
        "json_path": "$.workflow_rules[0].execute_when.details.repeat"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
