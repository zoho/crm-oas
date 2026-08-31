filters.value is not a boolean for a boolean key

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.filters.field.api_name"
    },
    "expected_data_type": "boolean",
    "api_name": "value",
    "json_path": "$.filters.value",
    "param_name": "filters"
  },
  "message": "dependent mismatch",
  "status": "error"
}
```
