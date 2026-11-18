INVALID_DATA error for below minimum length on the conversion_percentage_difference field

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
