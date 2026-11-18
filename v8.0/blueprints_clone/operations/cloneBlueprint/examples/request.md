### `application/json` — SamplePostRequest

Standalone clone of a Blueprint with state remapping

```json
{
  "blueprints": [
    {
      "name": "Autonum_Cloned",
      "type": "standalone",
      "layout": {
        "id": "5226917000000091023",
        "name": "Standard"
      },
      "field": {
        "id": "5226917000000002565",
        "api_name": "Stage"
      },
      "pipeline": {
        "id": "5226917000004004001",
        "name": "Standard (Standard)"
      },
      "map_states": [
        {
          "existing_state": {
            "actual_value": "-None-"
          },
          "clone_state": {
            "actual_value": "Qualification"
          }
        },
        {
          "existing_state": {
            "actual_value": "Option 1"
          },
          "clone_state": {
            "actual_value": "Needs Analysis"
          }
        },
        {
          "existing_state": {
            "actual_value": "Option 2"
          },
          "clone_state": {
            "actual_value": "Value Proposition"
          }
        }
      ],
      "module": "Potentials"
    }
  ]
}
```
