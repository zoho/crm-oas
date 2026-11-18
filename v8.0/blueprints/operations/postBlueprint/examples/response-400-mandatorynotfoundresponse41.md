MANDATORY_NOT_FOUND error for a missing module ID field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[*].transitions[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
