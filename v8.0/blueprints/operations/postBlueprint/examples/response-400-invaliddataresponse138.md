INVALID_DATA error for an invalid value in the owners field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "owners",
        "maximum_length": 2,
        "json_path": "$.blueprints[*].transitions[*].owners"
      },
      "status": "error"
    }
  ]
}
```
