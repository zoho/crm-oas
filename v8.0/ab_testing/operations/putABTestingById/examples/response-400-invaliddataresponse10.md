INVALID_DATA error for invalid data type on the name field

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].name"
      },
      "status": "error"
    }
  ]
}
```
