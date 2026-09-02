Section ID or api_name absent during a section operation

```json
{
  "layouts": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "_delete",
          "json_path": "$.layouts[0].sections[0]._delete"
        },
        "api_name": "api_name",
        "json_path": "$.layouts[0].sections[0].api_name"
      },
      "message": "section id or api_name is missing",
      "status": "error"
    }
  ]
}
```
