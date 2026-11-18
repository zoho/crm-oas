MANDATORY_NOT_FOUND error for a missing transition name

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.blueprints[*].transitions[*].name"
      },
      "status": "error"
    }
  ]
}
```
