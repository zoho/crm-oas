### `application/json` — Success

Example of mass convert request with two leads, Deal creation, tag carry-over, and related module transfer.

```json
{
  "ids": [
    "3652397000009850001",
    "3652397000009851001"
  ],
  "Deals": {
    "Deal_Name": "test7000"
  },
  "carry_over_tags": [
    {
      "id": "3652397000000002179",
      "api_name": "Contacts"
    },
    {
      "id": "3652397000000002180",
      "api_name": "Accounts"
    },
    {
      "id": "3652397000000002172",
      "api_name": "Deals"
    }
  ],
  "related_modules": [
    {
      "api_name": "Tasks",
      "id": "3652397000000002193"
    },
    {
      "api_name": "Events",
      "id": "3652397000000002195"
    },
    {
      "api_name": "Calls",
      "id": "3652397000000002197"
    }
  ],
  "assign_to": {
    "id": "3652397000000281001"
  },
  "move_attachments_to": {
    "api_name": "Contacts",
    "id": "3652397000000002179"
  }
}
```
