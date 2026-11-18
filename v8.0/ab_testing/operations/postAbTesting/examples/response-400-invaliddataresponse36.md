INVALID_DATA error: Invalid data (field: type)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "duration",
          "range",
          "visits"
        ],
        "json_path": "$.AB_testing[*].condition.type"
      },
      "status": "error"
    }
  ]
}
```
