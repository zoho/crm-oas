Example error for providing the same parent and child field.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].child.id"
      },
      "message": "The parent and child fieldid cannot be same",
      "status": "error"
    }
  ]
}
```
