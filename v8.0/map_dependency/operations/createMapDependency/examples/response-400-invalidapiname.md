Example of invalid field API name.

```json
{
  "map_dependency": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.map_dependency[0].parent.api_name"
      },
      "message": "The given api name is invalid",
      "status": "error"
    }
  ]
}
```
