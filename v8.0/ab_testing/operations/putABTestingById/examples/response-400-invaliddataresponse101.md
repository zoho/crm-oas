INVALID_DATA error for invalid data type on the conversion_percentage_difference field

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "conversion_percentage_difference",
        "expected_data_type": "integer",
        "json_path": "$.AB_testing[*].winner_configuration.conversion_percentage_difference"
      },
      "status": "error"
    }
  ]
}
```
