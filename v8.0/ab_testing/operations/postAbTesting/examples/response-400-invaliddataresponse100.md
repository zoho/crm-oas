INVALID_DATA error for unsupported value on announce_automatically

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "announce_automatically",
        "supported_values": [
          true,
          false
        ],
        "json_path": "$.AB_testing[*].winner_configuration.announce_automatically"
      },
      "status": "error"
    }
  ]
}
```
