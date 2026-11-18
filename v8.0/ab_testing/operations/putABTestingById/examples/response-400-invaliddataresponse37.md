INVALID_DATA: Invalid data (Field: type)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "period",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].condition.period"
      },
      "status": "error"
    }
  ]
}
```
