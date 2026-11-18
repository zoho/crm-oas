INVALID_DATA error for invalid data type on the traffic field

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "traffic",
        "expected_data_type": "integer",
        "json_path": "$.AB_testing[*].traffic"
      },
      "status": "error"
    }
  ]
}
```
