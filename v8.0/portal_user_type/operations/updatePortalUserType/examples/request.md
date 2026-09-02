### `application/json` — SamplePutRequest

Update portal user type

```json
{
  "user_type": [
    {
      "name": "Client Portal Updated",
      "active": true,
      "modules": [
        {
          "shared_type": "private",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": false,
            "create": true,
            "delete": true
          },
          "id": "111113000000002666",
          "filters": [
            {
              "id": "111113000000005092"
            }
          ],
          "layouts": [
            {
              "id": "111113000000003678",
              "_default_view": {
                "id": "111113000000003678",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000070019",
            "type": "canvas_view"
          }
        }
      ]
    }
  ]
}
```
