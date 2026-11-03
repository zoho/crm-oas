INVALID_DATA error — name field fails regex validation

```json
{
  "kiosks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "regex": "[0-9a-zA-Z_\\\\-\\\\.\\\\|\\\\$\\\\?\\\\,\\\\'\\\\/\\\\!\\\\P{InBasicLatin}\\\\s]+",
        "json_path": "$.kiosks[*].name"
      },
      "status": "error"
    }
  ]
}
```
