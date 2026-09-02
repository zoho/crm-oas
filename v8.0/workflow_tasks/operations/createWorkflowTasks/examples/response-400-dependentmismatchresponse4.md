Error response with code DEPENDENT_MISMATCH: Type and value is mismatched

```json
{
  "tasks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.tasks[0].field_mappings[0].type"
        },
        "api_name": "value",
        "json_path": "$.tasks[0].field_mappings[0].value"
      },
      "message": "Type and value is mismatched",
      "status": "error"
    }
  ]
}
```
