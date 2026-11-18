Error with code **DEPENDENT_FIELD_MISSING**: missing **parallel_transition**

```json
{
  "transitions": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "transition_type",
          "json_path": "$.transitions[0].transition_type"
        },
        "api_name": "parallel_transition",
        "json_path": "$.transitions[0].parallel_transition"
      },
      "message": "Dependent field is missing",
      "status": "error"
    }
  ]
}
```
