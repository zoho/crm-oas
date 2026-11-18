NOT_ALLOWED error for a missing dependent field on an include state

```json
{
  "blueprints": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "common",
          "json_path": "$.blueprints[0].connections[0].transitions.common"
        },
        "api_name": "include_states",
        "json_path": "$.blueprints[0].connections[0].transitions.include_states"
      },
      "message": "'include_states' required for common transitions",
      "status": "error"
    }
  ]
}
```
