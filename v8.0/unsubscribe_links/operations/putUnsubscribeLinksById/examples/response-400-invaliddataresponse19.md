INVALID_DATA error: unsupported page_type value

```json
{
  "unsubscribe_links": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "page_type",
        "supported_values": [
          "standard",
          "custom"
        ],
        "json_path": "$.unsubscribe_links[*].page_type"
      },
      "status": "error"
    }
  ]
}
```
