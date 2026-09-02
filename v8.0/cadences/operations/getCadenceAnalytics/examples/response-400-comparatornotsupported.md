Unsupported comparator value error

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.field.api_name"
    },
    "api_name": "comparator",
    "json_path": "$.comparator",
    "supported_values": [
      "equal"
    ],
    "param_name": "filters"
  },
  "message": "The value given seems to be invalid",
  "status": "error"
}
```
