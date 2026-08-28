# Examples: getRoles

**GET /settings/roles**

## Response examples

### Status `200` — `application/json` — Success

Successful roles retrieval response

```json
{
  "roles": [
    {
      "id": "4413524000000991001",
      "name": "Sales Manager",
      "display_label": "Sales Manager",
      "api_name": "sales_manager",
      "description": "Manages sales team and processes",
      "share_with_peers": true,
      "forecast_manager": {
        "id": "4413524000000991002",
        "name": "John Doe"
      },
      "reporting_to": {
        "id": "4413524000000991003",
        "name": "VP Sales"
      },
      "created_by__s": {
        "id": "4413524000000991004",
        "name": "Admin User"
      },
      "modified_by__s": {
        "id": "4413524000000991005",
        "name": "Admin User"
      },
      "modified_time__s": "2023-12-01T10:00:00Z",
      "created_time__s": "2023-11-01T09:00:00Z"
    }
  ]
}
```
