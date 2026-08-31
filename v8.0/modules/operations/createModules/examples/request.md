### `application/json` — MinimalModule

Create a custom module with required fields only

```json
{
  "modules": [
    {
      "plural_label": "CM123456",
      "singular_label": "CM123465",
      "api_name": "CustomModule1",
      "profiles": [
        {
          "id": "111111000000000497"
        }
      ]
    }
  ]
}
```

### `application/json` — ModuleWithTextDisplay

Create a module with a text display field

```json
{
  "modules": [
    {
      "plural_label": "CM1",
      "singular_label": "CM1",
      "api_name": "CustomModule2",
      "profiles": [
        {
          "id": "111111000000000497"
        }
      ],
      "display_field": {
        "field_label": "fieldLabel",
        "data_type": "text"
      }
    }
  ]
}
```

### `application/json` — ModuleWithAutonumber

Create a module with an auto-number display field including prefix and suffix

```json
{
  "modules": [
    {
      "plural_label": "CM21",
      "singular_label": "CM21",
      "api_name": "CustomModule3",
      "profiles": [
        {
          "id": "111111000000000497"
        }
      ],
      "display_field": {
        "field_label": "fieldLabel",
        "data_type": "autonumber",
        "auto_number": {
          "prefix": "M",
          "suffix": "H",
          "start_number": "21"
        }
      }
    }
  ]
}
```

### `application/json` — TeamBasedModule

Create a team-based custom module

```json
{
  "modules": [
    {
      "plural_label": "TeamModule1",
      "singular_label": "TeamModule1",
      "api_name": "TeamModule1",
      "access_type": "team_based"
    }
  ]
}
```
