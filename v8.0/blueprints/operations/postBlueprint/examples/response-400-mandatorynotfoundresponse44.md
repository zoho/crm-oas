MANDATORY_NOT_FOUND error for a missing field property

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "field",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.field"
      },
      "status": "error"
    }
  ]
}
```
