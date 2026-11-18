INVALID_DATA error for an invalid type field value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.blueprints[0].transition[0].transition_type",
        "supported_values": [
          "standalone_transition",
          "common_transition",
          "parallel_transition",
          "child_transition",
          "automatic_transition"
        ]
      },
      "message": "the value given is invalid",
      "status": "error"
    }
  ]
}
```
