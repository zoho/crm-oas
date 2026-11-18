INVALID_DATA error: 'type' field fails validation

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "static",
          "merge_field"
        ],
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```
