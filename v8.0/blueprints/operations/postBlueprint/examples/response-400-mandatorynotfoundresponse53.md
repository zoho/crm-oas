MANDATORY_NOT_FOUND error for a missing transition API name

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "api_name",
        "json_path": "$.blueprints[*].transitions[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
