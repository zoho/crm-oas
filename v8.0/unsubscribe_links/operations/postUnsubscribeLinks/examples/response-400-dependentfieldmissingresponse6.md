DEPENDENT_FIELD_MISSING error: Dependent field is missing (standard_page_message)

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
        "api_name": "standard_page_message",
        "json_path": "$.unsubscribe_links[*].unsubscribe_links.standard_page_message"
      },
      "status": "error"
    }
  ]
}
```
