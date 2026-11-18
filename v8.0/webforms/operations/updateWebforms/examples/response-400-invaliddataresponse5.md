INVALID_DATA returned when form width is outside the 600–900 range

```json
{
  "webforms": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "width",
        "json_path": "$.webforms[0].form_attributes.width",
        "range": {
          "from": 600,
          "to": 900
        }
      },
      "message": "form attribute width should be between 600 and 900",
      "status": "error"
    }
  ]
}
```
