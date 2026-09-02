### `application/json` — UpdatePermissions

Update permission enablement for a profile

```json
{
  "profiles": [
    {
      "name": "Updated Profile Name",
      "description": "Updated description for the profile.",
      "permissions_details": [
        {
          "id": "1408246000000063001",
          "enabled": false
        },
        {
          "id": "1408246000000057001",
          "enabled": true
        }
      ]
    }
  ]
}
```
