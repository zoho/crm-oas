DEPENDENT_MISMATCH error — unsupported comparator value in filters

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.group[0].field.api_name"
    },
    "api_name": "comparator",
    "json_path": "$.group[0].comparator",
    "supported_values": [
      "equal",
      "not_equal"
    ],
    "param_name": "filters"
  },
  "message": "The value given seems to be invalid",
  "status": "error"
}
```
