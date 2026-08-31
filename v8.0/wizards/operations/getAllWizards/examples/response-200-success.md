Successful retrieval of all configured wizards in the organization

```json
{
  "wizards": [
    {
      "created_time": "2025-11-26T08:59:44+05:30",
      "modified_time": "2025-11-26T15:58:16+05:30",
      "display_label": "Example Wizard",
      "portal_user_types": [
        {
          "display_label": "ClientPortal",
          "name": "ClientPortal",
          "id": "3733145000000570124"
        }
      ],
      "module": {
        "api_name": "Contacts",
        "id": "3733145000000570138"
      },
      "name": "example_wizard",
      "modified_by": {
        "name": "Alice",
        "id": "3733145000000556001"
      },
      "profiles": [
        {
          "name": "Administrator",
          "id": "3733145000000570117",
          "display_label": "Administrator"
        }
      ],
      "active": true,
      "source": "crm",
      "containers": [
        {
          "layout": {
            "name": "Standard",
            "display_label": "Standard",
            "id": "3733145000000570510"
          },
          "screens": [
            {
              "api_name": "screen1",
              "id": "3733145000001209037",
              "display_label": "Screen 1"
            }
          ],
          "id": "3733145000000570510"
        }
      ],
      "id": "3733145000001209011",
      "created_by": {
        "name": "Bob",
        "id": "3733145000000556001"
      }
    }
  ]
}
```
