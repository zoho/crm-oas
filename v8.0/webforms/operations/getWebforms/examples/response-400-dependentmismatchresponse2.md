Invalid data type for value parameter in filters

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "expected_data_type": "boolean",
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.group[0].field.api_name"
    },
    "api_name": "value",
    "json_path": "$.group[0].value",
    "param_name": "filters"
  },
  "message": "The value given seems to be invalid",
  "status": "error"
}
```
