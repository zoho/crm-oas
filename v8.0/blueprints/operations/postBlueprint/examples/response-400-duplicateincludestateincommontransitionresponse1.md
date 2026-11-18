DUPLICATE_DATA error for a common transition with a duplicate include state

```json
{
  "blueprints": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.blueprints[0].connections[0].transitions.include_states[1].state.api_name"
      },
      "message": "state already added as in include_states for the connection",
      "status": "error"
    }
  ]
}
```
