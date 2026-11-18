INVALID_DATA error: Invalid data (field: period)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "period",
        "supported_values": [
          "days",
          "weeks",
          "months"
        ],
        "json_path": "$.AB_testing[*].condition.period"
      },
      "status": "error"
    }
  ]
}
```
