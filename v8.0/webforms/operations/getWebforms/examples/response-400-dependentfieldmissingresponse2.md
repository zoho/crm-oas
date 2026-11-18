Missing required field parameter in filters

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.group[0].field"
    },
    "api_name": "field",
    "json_path": "$.group[0].field",
    "param_name": "filters"
  },
  "message": "Required Field missing",
  "status": "error"
}
```
