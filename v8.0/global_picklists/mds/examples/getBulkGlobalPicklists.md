# Examples: getBulkGlobalPicklists

**GET /settings/global_picklists**

## Parameter examples

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

### `inner_details_filters` (query) — `application/json` — SingleCriteria

Return only the unused picklist values of each global picklist

```json
[
  {
    "api_name": "pick_list_values",
    "filters": {
      "field": {
        "api_name": "type"
      },
      "comparator": "equal",
      "value": "unused"
    }
  }
]
```

### `inner_details_filters` (query) — `application/json` — NotEqualCriteria

Exclude the unused picklist values of each global picklist

```json
[
  {
    "api_name": "pick_list_values",
    "filters": {
      "field": {
        "api_name": "type"
      },
      "comparator": "not_equal",
      "value": "unused"
    }
  }
]
```

### `inner_details_filters` (query) — `application/json` — GroupOfCriteria

Filter the inner picklist values using multiple criteria combined with a group operator

```json
[
  {
    "api_name": "pick_list_values",
    "filters": {
      "group_operator": "or",
      "group": [
        {
          "field": {
            "api_name": "type"
          },
          "comparator": "equal",
          "value": "used"
        },
        {
          "field": {
            "api_name": "type"
          },
          "comparator": "equal",
          "value": "unused"
        }
      ]
    }
  }
]
```

### `filters` (query) — `application/json` — SingleCriteria

Filter the global picklists whose api_name is Industry

```json
{
  "field": {
    "api_name": "api_name"
  },
  "comparator": "equal",
  "value": "Industry"
}
```

### `filters` (query) — `application/json` — NotEqualCriteria

Filter the global picklists that are not created from CRM

```json
{
  "field": {
    "api_name": "source"
  },
  "comparator": "not_equal",
  "value": "crm"
}
```

### `filters` (query) — `application/json` — GroupOfCriteria

Filter using multiple criteria combined with a group operator

```json
{
  "group_operator": "and",
  "group": [
    {
      "field": {
        "api_name": "api_name"
      },
      "comparator": "equal",
      "value": "Industry"
    },
    {
      "field": {
        "api_name": "source"
      },
      "comparator": "equal",
      "value": "crm"
    }
  ]
}
```

### `filters` (query) — `application/json` — BooleanCriteria

Filter the global picklists that are customizable

```json
{
  "field": {
    "api_name": "customizable"
  },
  "comparator": "equal",
  "value": true
}
```

## Response examples

### Status `200` — `application/json` — GlobalPicklistsBulkMinimal

Minimal successful response

```json
{
  "global_picklists": [
    {
      "display_label": "Team Member Role",
      "api_name": "team_member_role__s",
      "customizable": false,
      "modified_by": null,
      "source": "crm",
      "description": null,
      "pick_list_values_sorted_lexically": false,
      "id": "4793076000000560088",
      "presence": true,
      "created_by": null,
      "actual_label": "Team Member Role",
      "modified_time": "2023-10-10T10:00:00Z",
      "created_time": "2023-10-01T09:00:00Z"
    },
    {
      "display_label": "Access",
      "api_name": "access__s",
      "customizable": false,
      "modified_by": null,
      "description": null,
      "source": "crm",
      "pick_list_values_sorted_lexically": false,
      "id": "4793076000000560089",
      "presence": true,
      "created_by": null,
      "actual_label": "Access",
      "modified_time": "2023-10-10T10:00:00Z",
      "created_time": "2023-10-01T09:00:00Z"
    }
  ]
}
```

### Status `200` — `application/json` — GlobalPicklistsBulkExpanded

Expanded response when include=pick_list_values,used_in_modules,associated_fields_count

```json
{
  "global_picklists": [
    {
      "display_label": "Team Member Role",
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
      "source": "crm",
      "pick_list_values_sorted_lexically": false,
      "id": "4793076000000560088",
      "presence": true,
      "created_by": null,
      "actual_label": "Team Member Role",
      "pick_list_values": [
        {
          "display_value": "Owner",
          "sequence_number": 1,
          "actual_value": "Owner",
          "reference_value": "Owner",
          "id": "4793076000000564764",
          "type": "used"
        },
        {
          "display_value": "Admin",
          "sequence_number": 2,
          "actual_value": "Admin",
          "id": "4793076000000564765",
          "reference_value": "Admin",
          "type": "used"
        },
        {
          "display_value": "Member",
          "sequence_number": 3,
          "actual_value": "Member",
          "reference_value": "Member",
          "id": "4793076000000564766",
          "type": "unused"
        }
      ],
      "modified_time": "2023-10-10T10:00:00Z",
      "created_time": "2023-10-01T09:00:00Z"
    },
    {
      "display_label": "Access",
      "api_name": "access__s",
      "customizable": false,
      "modified_by": null,
      "description": null,
      "source": "crm",
      "pick_list_values_sorted_lexically": false,
      "id": "4793076000000560089",
      "presence": true,
      "created_by": null,
      "actual_label": "Access",
      "pick_list_values": [
        {
          "display_value": "Private",
          "sequence_number": 1,
          "actual_value": "Private",
          "reference_value": "Private",
          "id": "4793076000000564770",
          "type": "used"
        },
        {
          "display_value": "Public Read Only",
          "sequence_number": 2,
          "actual_value": "Public Read Only",
          "reference_value": "Public Read Only",
          "id": "4793076000000564771",
          "type": "used"
        },
        {
          "display_value": "Public Read/Write",
          "sequence_number": 3,
          "actual_value": "Public Read/Write",
          "reference_value": "Public Read/Write",
          "id": "4793076000000564772",
          "type": "unused"
        }
      ],
      "modified_time": "2023-10-10T10:00:00Z",
      "created_time": "2023-10-01T09:00:00Z"
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
    },
    {
      "display_label": "Access",
      "api_name": "access__s",
      "customizable": false,
      "id": "4793076000000560089"
    },
    {
      "display_label": "Industry",
      "api_name": "Industry",
      "customizable": true,
      "id": "4793076000000560090"
    }
  ]
}
```

### Status `200` — `application/json` — GlobalPicklistsFilteredByValue

Response when filters selects a single global picklist by api_name

```json
{
  "global_picklists": [
    {
      "display_label": "Industry",
      "api_name": "Industry",
      "actual_label": "Industry",
      "customizable": true,
      "description": null,
      "source": "crm",
      "pick_list_values_sorted_lexically": false,
      "presence": true,
      "created_by": null,
      "modified_by": null,
      "created_time": null,
      "modified_time": null,
      "id": "4793076000000560090"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonarray",
    "param_name": "inner_details_filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponseApiName

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: api_name)

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "api_name",
    "json_path": "$.inner_details_filters[0].api_name",
    "param_name": "inner_details_filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponseFilters

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: filters)

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "filters",
    "json_path": "$.inner_details_filters[0].filters",
    "param_name": "inner_details_filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponseField

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: field)

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "field",
    "json_path": "$.inner_details_filters[0].filters.field",
    "param_name": "inner_details_filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponseFieldApiName

Error response with code MANDATORY_NOT_FOUND: required field not found (Field: field.api_name)

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "api_name",
    "json_path": "$.inner_details_filters[0].filters.field.api_name",
    "param_name": "inner_details_filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: invalid data (Field: api_name)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "api_name",
    "json_path": "$.inner_details_filters[0].api_name",
    "param_name": "inner_details_filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: invalid data (Field: filters)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "filters",
    "expected_data_type": "jsonobject",
    "json_path": "$.inner_details_filters[0].filters",
    "param_name": "inner_details_filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Error response with code INVALID_DATA: The value given is not supported (Field: comparator)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "comparator",
    "json_path": "$.inner_details_filters[0].filters.comparator",
    "supported_values": [
      "equal",
      "not_equal"
    ],
    "param_name": "inner_details_filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Error response with code DEPENDENT_MISMATCH: dependent mismatch (Field: value)

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.inner_details_filters[0].filters.field.api_name"
    },
    "expected_data_type": "boolean",
    "api_name": "value",
    "json_path": "$.inner_details_filters[0].filters.value",
    "param_name": "inner_details_filters"
  },
  "message": "dependent mismatch",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: comparator)

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.inner_details_filters[0].filters.field"
    },
    "api_name": "comparator",
    "json_path": "$.inner_details_filters[0].filters.comparator",
    "param_name": "inner_details_filters"
  },
  "message": "Dependent Field missing",
  "status": "error"
}
```

### Status `400` — `application/json` — NotSupportedFieldResponse1

Error response with code NOT_SUPPORTED: The value given is not supported (Field: api_name)

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "api_name": "api_name",
    "json_path": "$.inner_details_filters[0].filters.field.api_name",
    "param_name": "inner_details_filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — NotSupportedFieldResponse2

Error response with code NOT_SUPPORTED: The value given is not supported (Field: api_name in nested group)

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "api_name": "api_name",
    "json_path": "$.inner_details_filters[0].filters.group[1].field.api_name",
    "param_name": "inner_details_filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidGroupOperatorResponse1

Error response with code INVALID_DATA: invalid data (Field: group_operator)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.inner_details_filters[0].filters.group_operator",
    "supported_values": [
      "and",
      "or"
    ],
    "param_name": "inner_details_filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersNotAJsonObject

filters is empty

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonobject",
    "param_name": "filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersFieldNotFound

field is not given inside filters

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "field",
    "json_path": "$.filters.field",
    "param_name": "filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersFieldApiNameNotFound

api_name is not given inside filters.field

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "api_name",
    "json_path": "$.filters.field.api_name",
    "param_name": "filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersComparatorMissing

comparator is not given along with field

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.filters.field"
    },
    "api_name": "comparator",
    "json_path": "$.filters.comparator",
    "param_name": "filters"
  },
  "message": "Dependent Field missing",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersValueMissing

value is not given along with field

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.filters.field"
    },
    "api_name": "value",
    "json_path": "$.filters.value",
    "param_name": "filters"
  },
  "message": "Dependent Field missing",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersFieldApiNameNotSupported

The key given in filters.field.api_name cannot be filtered

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "api_name": "api_name",
    "json_path": "$.filters.field.api_name",
    "param_name": "filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersComparatorNotSupported

Unsupported comparator given in filters

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "comparator",
    "json_path": "$.filters.comparator",
    "supported_values": [
      "not_equal",
      "equal"
    ],
    "param_name": "filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersValueDataTypeMismatch

filters.value is not a string for a string key

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.filters.field.api_name"
    },
    "expected_data_type": "string",
    "api_name": "value",
    "json_path": "$.filters.value",
    "param_name": "filters"
  },
  "message": "dependent mismatch",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersComparatorNotSupportedForBooleanKey

Unsupported comparator given for a boolean key in filters

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "comparator",
    "json_path": "$.filters.comparator",
    "supported_values": [
      "equal"
    ],
    "param_name": "filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersValueNotABoolean

filters.value is not a boolean for a boolean key

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.filters.field.api_name"
    },
    "expected_data_type": "boolean",
    "api_name": "value",
    "json_path": "$.filters.value",
    "param_name": "filters"
  },
  "message": "dependent mismatch",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupOperatorNotFound

group is given without group_operator

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.filters.group_operator",
    "param_name": "filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupNotFound

group_operator is given without group

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "group",
    "json_path": "$.filters.group",
    "param_name": "filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupNotAJsonArray

filters.group is not a JSON array

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonarray",
    "api_name": "group",
    "json_path": "$.filters.group",
    "param_name": "filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupFieldNotAJsonObject

field inside a group criteria is not a JSON object

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonobject",
    "api_name": "field",
    "json_path": "$.filters.group[1].field",
    "param_name": "filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupFieldNotFound

field is not given inside a group criteria

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "field",
    "json_path": "$.filters.group[1].field",
    "param_name": "filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupFieldApiNameNotSupported

The key given inside a group criteria cannot be filtered

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "api_name": "api_name",
    "json_path": "$.filters.group[1].field.api_name",
    "param_name": "filters"
  },
  "message": "The value given is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersGroupOperatorNotSupported

Unsupported group_operator given in filters

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "group_operator",
    "json_path": "$.filters.group_operator",
    "supported_values": [
      "and",
      "or"
    ],
    "param_name": "filters"
  },
  "message": "invalid data",
  "status": "error"
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
