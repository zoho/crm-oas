INVALID_DATA error when conversion_percentage_difference exceeds the maximum

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "conversion_percentage_difference",
        "maximum_length": 2,
        "json_path": "$.AB_testing[*].winner_configuration.conversion_percentage_difference"
      },
      "status": "error"
    }
  ]
}
```
