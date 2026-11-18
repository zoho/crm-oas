INVALID_DATA error: Invalid data type (field: to)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "to",
        "expected_data_type": "datetime",
        "json_path": "$.AB_testing[*].condition.to"
      },
      "status": "error"
    }
  ]
}
```
