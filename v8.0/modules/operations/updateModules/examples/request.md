### `application/json` — RemoveAndAddProfile

Remove admin profile and add standard profile for a custom module

```json
{
  "modules": [
    {
      "singular_label": "CMUpdated",
      "plural_label": "CMUpdated",
      "id": "111111000000263276",
      "profiles": [
        {
          "id": "111111000000000497",
          "_delete": null
        },
        {
          "id": "111111000000000499"
        }
      ]
    }
  ]
}
```

### `application/json` — BatchUpdateMixedOperations

Batch update with label changes and profile modifications

```json
{
  "modules": [
    {
      "singular_label": "CMUpdated",
      "plural_label": "CMUpdated",
      "id": "111111000000263276",
      "profiles": [
        {
          "id": "111111000000000497"
        },
        {
          "id": "111111000000000499",
          "_delete": null
        }
      ]
    },
    {
      "id": "111111000000258973",
      "plural_label": "CM2Updated",
      "singular_label": "CM2Updated"
    }
  ]
}
```

### `application/json` — UpdateLabelsOnly

Update module labels without changing profiles

```json
{
  "modules": [
    {
      "id": "111111000000002654",
      "plural_label": "DealsUpdated",
      "singular_label": "DealUpdated"
    }
  ]
}
```

### `application/json` — RemoveProfileOnly

Remove profile access without updating labels

```json
{
  "modules": [
    {
      "id": "111111000000002654",
      "profiles": [
        {
          "id": "111111000000000497",
          "_delete": null
        }
      ]
    }
  ]
}
```
