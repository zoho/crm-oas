INVALID_DATA error returned for an id value of the wrong data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
