Error response with code INVALID_DATA: workflow name exceeds max length

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.workflow_rules[*].name",
        "maximum_length": 100
      },
      "message": "value too long",
      "status": "error"
    }
  ]
}
```
