Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "triggers",
          "json_path": "$.cadences[0].follow_ups[1].triggers[0]"
        },
        "api_name": "execute_after",
        "json_path": "$.cadences[0].follow_ups[1].execute_after"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
