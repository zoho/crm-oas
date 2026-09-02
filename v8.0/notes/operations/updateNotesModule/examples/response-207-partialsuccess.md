Partial success - some notes updated, some failed

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-05T14:27:48+05:30",
        "Modified_By": {
          "name": "Prasanna CEO",
          "id": "111111000000059489"
        },
        "Created_Time": "2026-01-05T14:27:48+05:30",
        "id": "111111000000116018",
        "Created_By": {
          "name": "Prasanna CEO",
          "id": "111111000000059489"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "Note_Content",
            "json_path": "$.data[1].Note_Content"
          },
          {
            "api_name": "Note_Title",
            "json_path": "$.data[1].Note_Title"
          }
        ]
      },
      "message": "should contain either content or title",
      "status": "error"
    }
  ]
}
```
