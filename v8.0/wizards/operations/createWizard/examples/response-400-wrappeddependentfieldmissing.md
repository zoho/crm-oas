Wrapped dependent field missing — e.g., conditional rules depend on screens

```json
{
  "wizards": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "conditional_rules",
        "json_path": "$.wizards[0].screens[0].conditional_rules",
        "dependee": {
          "api_name": "screens",
          "json_path": "$.wizards[0].screens"
        }
      },
      "message": "Dependent field missing",
      "status": "error"
    }
  ]
}
```
