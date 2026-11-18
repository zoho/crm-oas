INVALID_DATA error for an unsupported transition_type value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "transition_type",
        "supported_values": [
          "standalone_transition",
          "parallel_transition",
          "child_transition"
        ],
        "json_path": "$.blueprints[*].transitions[*].transition_type"
      },
      "status": "error"
    }
  ]
}
```
