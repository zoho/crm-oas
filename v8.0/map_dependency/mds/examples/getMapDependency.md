# Examples: getMapDependency

**GET /settings/layouts/{layoutId}/map_dependency**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Example of a successful response with field dependencies.

```json
{
  "map_dependency": [
    {
      "parent": {
        "api_name": "Lead_Source",
        "id": "1043386000000002609"
      },
      "internal": false,
      "sub_module": null,
      "active": true,
      "id": "1043386000020283001",
      "source": 1,
      "category": 0,
      "child": {
        "api_name": "Lead_Status",
        "id": "1043386000000002611"
      }
    },
    {
      "parent": {
        "api_name": "Pick_List_1",
        "id": "1043386000019791055"
      },
      "internal": false,
      "sub_module": {
        "api_name": "Subform_3",
        "id": "1043386000016645081"
      },
      "active": true,
      "id": "1043386000020283005",
      "source": 1,
      "category": 0,
      "child": {
        "api_name": "Pick_List_2",
        "id": "1043386000019791245"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 2,
    "page": 1,
    "more_records": false
  }
}
```

### Status `200` — `application/json` — InactiveDependencyResponse

Example of a successful response containing an inactive field dependency.

```json
{
  "map_dependency": [
    {
      "parent": {
        "api_name": "Salutation",
        "id": "1043386000000002601"
      },
      "internal": false,
      "sub_module": null,
      "active": false,
      "id": "1043386000020283009",
      "source": 1,
      "category": 0,
      "child": {
        "api_name": "Industry",
        "id": "1043386000000003402"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — RequiredParamMissing

Example of required parameter missing.

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Example of invalid module name.

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidLayoutId

Example of invalid layout ID.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "Invalid Layout Id",
  "status": "error"
}
```

### Status `400` — `application/json` — LayoutDeactivated

Example of deactivated layout.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The layout is deactivated",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidFilterValue

Example of an invalid filters parameter value.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "filters",
    "json_path": "$",
    "param_name": "filters"
  },
  "message": "the value given is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidComparator

Example of invalid filter comparator value.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "comparator",
    "json_path": "$.comparator",
    "supported_values": [
      "equal",
      "in"
    ],
    "param_name": "filters"
  },
  "message": "The value given is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissing

Example of dependent field missing in filter.

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.field"
    },
    "api_name": "comparator",
    "json_path": "$.comparator",
    "param_name": "filters"
  },
  "message": "Dependent Field missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFound

Example of mandatory filter field missing.

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "api_name",
    "json_path": "$.field.api_name",
    "param_name": "filters"
  },
  "message": "Required field not found",
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

Example of an internal server error.

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
