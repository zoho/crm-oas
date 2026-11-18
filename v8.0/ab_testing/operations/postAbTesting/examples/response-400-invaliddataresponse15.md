INVALID_DATA error for invalid data type on the notify field

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "notify",
        "expected_data_type": "boolean",
        "json_path": "$.AB_testing[*].notify"
      },
      "status": "error"
    }
  ]
}
```
