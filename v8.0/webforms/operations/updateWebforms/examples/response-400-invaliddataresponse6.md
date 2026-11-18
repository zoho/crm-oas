INVALID_DATA returned when font size is outside the 11–16 range

```json
{
  "webforms": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "width",
        "json_path": "$.webforms[0].form_attributes.font_attributes.size",
        "range": {
          "from": 11,
          "to": 16
        }
      },
      "message": "font attribute size should be between 11 and 16",
      "status": "error"
    }
  ]
}
```
