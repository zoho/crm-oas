Error response with code INVALID_DATA: Invalid data (Field: transition_type)

```json
{
  "transitions": [
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
        "json_path": "$.transitions[*].transition_type"
      },
      "status": "error"
    }
  ]
}
```
