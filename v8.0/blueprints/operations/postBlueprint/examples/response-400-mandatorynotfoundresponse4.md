MANDATORY_NOT_FOUND error for a missing owner resource ID

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[*].owners[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
