DUPLICATE_DATA error for a state with a duplicate api_name

```json
{
  "blueprints": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.blueprint[0].state[2].api_name"
      },
      "message": "a different state with same api_name found",
      "status": "error"
    }
  ]
}
```
