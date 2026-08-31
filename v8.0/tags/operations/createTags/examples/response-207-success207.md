Partial success response for tag creation

```json
{
  "tags": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.tags[0].name",
        "id": "111111000000116258"
      },
      "message": "duplicate data",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "created_time": "2025-12-29T17:59:54+05:30",
        "modified_time": "2025-12-29T17:59:54+05:30",
        "name": "Newtag2",
        "modified_by": {
          "name": "Roobini Devi",
          "id": "111111000000059475"
        },
        "id": "111111000000116262",
        "created_by": {
          "name": "Roobini Devi",
          "id": "111111000000059475"
        },
        "color_code": null
      },
      "message": "tags created successfully",
      "status": "success"
    }
  ]
}
```
