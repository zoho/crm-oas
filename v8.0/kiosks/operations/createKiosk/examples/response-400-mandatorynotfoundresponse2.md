MANDATORY_NOT_FOUND error when the required name field is missing from a kiosk item

```json
{
  "kiosks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.kiosks[*].name"
      },
      "status": "error"
    }
  ]
}
```
