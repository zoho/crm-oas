INVALID_DATA: Invalid data type (Field: type)

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
