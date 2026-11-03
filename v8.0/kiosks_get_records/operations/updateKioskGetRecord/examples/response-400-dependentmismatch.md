Selection range should be 1 for single record

```json
{
  "get_records": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "result_type",
          "json_path": "$.get_records[0].selection_details.result_type"
        },
        "api_name": "range",
        "json_path": "$.get_records[0].selection_details.range",
        "maximum_value": 1
      },
      "message": "Get Record selection range should be 1 for single record",
      "status": "error"
    }
  ]
}
```
