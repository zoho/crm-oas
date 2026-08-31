Example error of dependency creating a loop.

```json
{
  "map_dependency": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.map_dependency[0].child.id"
      },
      "message": "The given child field when associated with this parent field will result in loop",
      "status": "error"
    }
  ]
}
```
