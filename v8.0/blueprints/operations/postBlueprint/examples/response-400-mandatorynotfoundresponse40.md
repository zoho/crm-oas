MANDATORY_NOT_FOUND error for a missing trigger_type field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "trigger_type",
        "json_path": "$.blueprints[*].transitions[*].trigger_type"
      },
      "status": "error"
    }
  ]
}
```
