Error response with code NOT_ALLOWED: the from state and to state of the transition are the same (Field: api_name)

```json
{
  "blueprints": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.bluperint[0].chart_data.connections[0].from.state.api_name"
      },
      "message": "From state and to state of the transition seems to be the same state",
      "status": "error"
    }
  ]
}
```
