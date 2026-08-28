# Examples: getSingleGlobalPicklists

**GET /settings/global_picklists/{id}**

## Parameter examples

### `id` (path) — Example

```json
"111111000000055938"
```

### `include` (query) — Single

Single value

```json
[
  "used_in_modules"
]
```

### `include` (query) — Multiple

Multiple values (CSV)

```json
[
  "used_in_modules",
  "associated_fields_count"
]
```

### `include_inner_details` (query) — Example

plural label will be included in used_in_modules

```json
"used_in_modules.plural_label"
```

### `fields` (query) — Single

Single key

```json
[
  "display_label"
]
```

### `fields` (query) — Multiple

Multiple keys (CSV)

```json
[
  "display_label",
  "api_name",
  "customizable"
]
```

## Response examples

### Status `200` — `application/json` — GlobalPicklistsMinimal

Minimal successful response

```json
{
  "global_picklists": [
    {
      "display_label": "Team Member Role",
      "api_name": "team_member_role__s",
      "customizable": false,
      "modified_by": null,
      "description": null,
      "source": "crm",
      "pick_list_values_sorted_lexically": false,
      "id": "4793076000000560088",
      "presence": true,
      "created_by": null,
      "actual_label": "Team Member Role",
      "modified_time": "2023-10-10T10:00:00Z",
      "created_time": "2023-10-01T09:00:00Z",
      "pick_list_values": [
        {
          "display_value": "Owner",
          "sequence_number": 1,
          "reference_value": "Owner",
          "actual_value": "Owner",
          "id": "4793076000000564764",
          "type": "used"
        },
        {
          "display_value": "Admin",
          "sequence_number": 2,
          "reference_value": "Admin",
          "actual_value": "Admin",
          "id": "4793076000000564765",
          "type": "used"
        },
        {
          "display_value": "Member",
          "sequence_number": 3,
          "reference_value": "Member",
          "actual_value": "Member",
          "id": "4793076000000564766",
          "type": "unused"
        }
      ]
    }
  ]
}
```

### Status `200` — `application/json` — GlobalPicklistsExpanded

Expanded response when include=pick_list_values,used_in_modules,associated_fields_count

```json
{
  "global_picklists": [
    {
      "display_label": "Team Member Role",
      "modified_time": "2023-10-10T10:00:00Z",
      "created_time": "2023-10-01T09:00:00Z",
      "source": "crm",
      "used_in_modules": [
        {
          "plural_label": "Preferred Team Members",
          "api_name": "Preferred_Team_Members__s",
          "id": "4793076000000559061"
        },
        {
          "plural_label": "Team Selling",
          "api_name": "Team_Selling__s",
          "id": "4793076000000559062"
        }
      ],
      "api_name": "team_member_role__s",
      "customizable": false,
      "modified_by": null,
      "description": null,
      "pick_list_values_sorted_lexically": false,
      "id": "4793076000000560088",
      "presence": true,
      "created_by": null,
      "actual_label": "Team Member Role",
      "pick_list_values": [
        {
          "display_value": "Owner",
          "sequence_number": 1,
          "reference_value": "Owner",
          "actual_value": "Owner",
          "id": "4793076000000564764",
          "type": "used"
        },
        {
          "display_value": "Admin",
          "sequence_number": 2,
          "reference_value": "Admin",
          "actual_value": "Admin",
          "id": "4793076000000564765",
          "type": "used"
        },
        {
          "display_value": "Member",
          "sequence_number": 3,
          "reference_value": "Member",
          "actual_value": "Member",
          "id": "4793076000000564766",
          "type": "unused"
        }
      ]
    }
  ]
}
```

### Status `200` — `application/json` — GlobalPicklistsFilteredByKey

Response when fields=display_label,api_name,customizable

```json
{
  "global_picklists": [
    {
      "display_label": "Team Member Role",
      "api_name": "team_member_role__s",
      "customizable": false,
      "id": "4793076000000560088"
    }
  ]
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
