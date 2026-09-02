### `application/json` — RenameLayout

Rename an existing custom layout

```json
{
  "layouts": [
    {
      "name": "Updated CL1"
    }
  ]
}
```

### `application/json` — AddProfilePermission

Granting a CRM profile access to a layout

```json
{
  "layouts": [
    {
      "profiles": [
        {
          "id": "111111000000000395"
        }
      ]
    }
  ]
}
```

### `application/json` — RemoveProfilePermission

Revokes a CRM profile's access to a layout via the delete flag

```json
{
  "layouts": [
    {
      "profiles": [
        {
          "id": "111111000000000393",
          "_delete": true
        }
      ]
    }
  ]
}
```

### `application/json` — ToggleBusinessCard

Toggle the business card display setting on a layout

```json
{
  "layouts": [
    {
      "show_business_card": false
    }
  ]
}
```

### `application/json` — CreateCustomSection

Creating a new custom section within a layout

```json
{
  "layouts": [
    {
      "sections": [
        {
          "sequence_number": 6,
          "tab_traversal": "left_to_right",
          "column_count": 1,
          "name": "Custom Section 2",
          "display_label": "Custom Section 2"
        }
      ]
    }
  ]
}
```

### `application/json` — AddFieldToSection

Adding an existing field to a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3722469000001347394"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — UpdateFieldSequence

Reorder a field's position within a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3722469000001347394",
              "sequence_number": 2
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — DeleteSection

Permanently removes a section and its field assignments from a layout

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "_delete": {
            "permanent": true
          }
        }
      ]
    }
  ]
}
```

### `application/json` — MoveFieldToUnused

Relocates a field to the unused items section without deleting it

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "id": "3722469000001347394",
              "_delete": {
                "permanent": false
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — CreateNewField

Adds a new custom field definition to a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "field_label": "CF1",
              "length": 16,
              "sequence_number": 1,
              "data_type": "text"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — MultipleFieldsAcrossSections

Adds up to five fields spread across multiple layout sections in one request

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3722469000001347394"
            },
            {
              "id": "3722469000001347395"
            }
          ]
        },
        {
          "id": "3722469000001374015",
          "fields": [
            {
              "id": "3722469000001347396"
            },
            {
              "id": "3722469000001347397"
            },
            {
              "id": "3722469000001347398"
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — CreateFieldWithAssociation

Creating a new field with a Field-Of-Lookup association

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "field_label": "Account Revenue",
              "data_type": "integer",
              "length": 9,
              "association_details": {
                "lookup_field": {
                  "id": "3722469000001347500",
                  "api_name": "Account_Lookup"
                },
                "related_field": {
                  "id": "3722469000001347600",
                  "api_name": "Annual_Revenue"
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — UpdateFieldWithAssociation

Attach a Field-Of-Lookup association to an existing layout field

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001347180",
          "fields": [
            {
              "id": "3722469000001347394",
              "association_details": {
                "lookup_field": {
                  "id": "3722469000001347500"
                },
                "related_field": {
                  "id": "3722469000001347600"
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### `application/json` — AddMirrorComponentToSection

Adding a mirror field component to a layout section

```json
{
  "layouts": [
    {
      "sections": [
        {
          "id": "3722469000001374014",
          "fields": [
            {
              "id": "3359388011000000523",
              "sequence_number": 3,
              "element_type": "mirror_field",
              "lookup_field": {
                "id": "3359388000000000523",
                "api_name": "Account_Name"
              }
            }
          ]
        }
      ]
    }
  ]
}
```
