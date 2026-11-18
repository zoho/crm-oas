MANDATORY_NOT_FOUND error for a missing criteria field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "criteria",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria"
      },
      "status": "error"
    }
  ]
}
```
