INVALID_DATA error when traffic value is below the minimum

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "traffic",
        "minimum_length": 1,
        "json_path": "$.AB_testing[*].traffic"
      },
      "status": "error"
    }
  ]
}
```
