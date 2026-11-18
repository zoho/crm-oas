INVALID_DATA error when conversion_percentage_difference is below the minimum

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "conversion_percentage_difference",
        "minimum_length": 1,
        "json_path": "$.AB_testing[*].winner_configuration.conversion_percentage_difference"
      },
      "status": "error"
    }
  ]
}
```
