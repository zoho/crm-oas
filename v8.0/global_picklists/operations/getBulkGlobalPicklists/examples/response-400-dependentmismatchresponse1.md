Error response with code DEPENDENT_MISMATCH: dependent mismatch (Field: value)

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.inner_details_filters[0].filters.field.api_name"
    },
    "expected_data_type": "boolean",
    "api_name": "value",
    "json_path": "$.inner_details_filters[0].filters.value",
    "param_name": "inner_details_filters"
  },
  "message": "dependent mismatch",
  "status": "error"
}
```
