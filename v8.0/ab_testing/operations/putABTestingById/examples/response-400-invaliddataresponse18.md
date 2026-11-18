INVALID_DATA: Invalid data (Field: status)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "status",
        "supported_values": [
          "drafted",
          "running",
          "scheduled"
        ],
        "json_path": "$.AB_testing[*].status"
      },
      "status": "error"
    }
  ]
}
```
