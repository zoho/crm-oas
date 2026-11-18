INVALID_DATA error: Invalid data type (field: type)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].condition.type"
      },
      "status": "error"
    }
  ]
}
```
