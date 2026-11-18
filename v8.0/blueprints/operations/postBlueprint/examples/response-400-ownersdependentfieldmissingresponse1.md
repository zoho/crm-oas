Error response with code NOT_ALLOWED: owners is a required dependent field when continuous is specified but not given (Field: owners)

```json
{
  "blueprints": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "continuous",
          "json_path": "$.blueprints[0].continuous"
        },
        "api_name": "owners",
        "json_path": "$.blueprints[0].owners"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```
