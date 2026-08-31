DEPENDENT_FIELD_MISSING error: Dependent field is missing (custom_location_url)

```json
{
  "unsubscribe_links": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "page_type",
          "json_path": "$.unsubscribe_links[*].page_type"
        },
        "api_name": "custom_location_url",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.custom_location_url"
      },
      "status": "error"
    }
  ]
}
```
