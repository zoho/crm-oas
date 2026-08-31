Status field rejected due to incorrect data type instead of expected text.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Status",
        "expected_data_type": "text",
        "json_path": "$.data[*].Status"
      },
      "status": "error"
    }
  ]
}
```
