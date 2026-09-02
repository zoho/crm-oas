### `application/json` — Sample

An example of the schedule deletion of a single tag from the Leads module.

```json
{
  "mass_delete": [
    {
      "module": {
        "api_name": "Leads",
        "id": "123"
      },
      "tags": [
        {
          "id": "456",
          "name": "Priority"
        }
      ]
    }
  ]
}
```
