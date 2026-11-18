INVALID_DATA error for invalid data type on the module ID field

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.AB_testing[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
