Dependent field missing when custom_view is provided without based_on

```json
{
  "run_rules": {
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "based_on",
        "json_path": "$.run_rules.based_on"
      },
      "api_name": "id",
      "json_path": "$.run_rules.custom_view"
    },
    "message": "Dependent Field missing",
    "status": "error"
  }
}
```
