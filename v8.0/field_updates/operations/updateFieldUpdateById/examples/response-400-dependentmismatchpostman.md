Error response with code DEPENDENT_MISMATCH: Dependent Field is not matching

```json
{
  "field_updates": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.field_updates[0].field"
        },
        "api_name": "value",
        "json_path": "$.field_updates[0].value"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```
