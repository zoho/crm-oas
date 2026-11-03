INVALID_DATA error — unsupported value for type field

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "dependent",
          "standalone"
        ],
        "json_path": "$.kiosks[*].type"
      },
      "status": "error"
    }
  ]
}
```
