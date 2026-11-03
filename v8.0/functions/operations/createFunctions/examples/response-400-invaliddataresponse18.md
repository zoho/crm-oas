INVALID_DATA Error for Unsupported Runtime Value

```json
{
  "functions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "runtime",
        "supported_values": [
          "Deluge 1.0",
          "Java 8",
          "Java 17",
          "NodeJS 8",
          "NodeJS 22",
          "Python 3.12"
        ],
        "json_path": "$.functions[*].runtime"
      },
      "status": "error"
    }
  ]
}
```
