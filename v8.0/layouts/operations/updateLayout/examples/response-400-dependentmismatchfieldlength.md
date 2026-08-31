Field length and related field length incompatible for FoL mapping

```json
{
  "layouts": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "length",
          "json_path": "$.layouts[0].sections[0].fields[0].length"
        },
        "api_name": "id",
        "json_path": "$.layouts[0].sections[0].fields[0].association_details.related_field.id"
      },
      "message": "Field length mismatch for FOL mapping",
      "status": "error"
    }
  ]
}
```
