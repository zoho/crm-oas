# Examples: updateFiscalYear

**PUT /settings/fiscal_year**

## Request examples

### `application/json` — SwitchToStandardFiscalYear

Switch from a custom fiscal year to a standard fiscal year

```json
{
  "fiscal_year": {
    "calendar_type": "gregorian"
  }
}
```

## Response examples

### Status `200` — `application/json` — Success200

Fiscal year settings updated successfully

```json
{
  "fiscal_year": {
    "code": "SUCCESS",
    "details": {
      "id": "111111000000008761"
    },
    "message": "The fiscal year configuration has been updated successfully",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — Error400Response1

Invalid start_date error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "start_date",
      "json_path": "$.fiscal_year.start_date"
    },
    "message": "Please give a valid start_date",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response2

Invalid structure error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "structure",
      "json_path": "$.fiscal_year.structure",
      "supported_values": [
        "4-4-5",
        "4-5-4",
        "5-4-4",
        "3-3-3-4",
        "3-3-4-3",
        "3-4-3-3",
        "4-3-3-3"
      ]
    },
    "message": "Please give a valid structure",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response3

Invalid interval_display_option error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "interval_display_option",
      "json_path": "$.fiscal_year.interval_display_option",
      "supported_values": [
        "year",
        "quarter"
      ]
    },
    "message": "Please give a valid number_by display option",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response4

Mismatched start_date and start_month error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "start_date",
      "json_path": "$.fiscal_year.start_date"
    },
    "message": "start_date does not match with start_month",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response5

Surplus week cannot be configured for gregorian calendar error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "surplus_week",
      "json_path": "$.fiscal_year.surplus_week"
    },
    "message": "cannot configure surplus week for gregorian calendar",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response6

Invalid start_month error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "INVALID_DATA",
    "message": "Please give a valid month",
    "details": {
      "supported_values": [
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER"
      ],
      "api_name": "start_month",
      "json_path": "$.fiscal_year.start_month"
    }
  }
}
```

### Status `400` — `application/json` — Error400Response7

Invalid display_based_on error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "INVALID_DATA",
    "message": "Please give a valid display based on",
    "details": {
      "supported_values": [
        "start_month",
        "end_month"
      ],
      "api_name": "display_based_on",
      "json_path": "$.fiscal_year.display_based_on"
    }
  }
}
```

### Status `400` — `application/json` — Error400Response8

Invalid calendar_type value error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "calendar_type",
      "json_path": "$.fiscal_year.calendar_type",
      "supported_values": [
        "gregorian",
        "custom"
      ]
    },
    "message": "Please give a valid calendar type",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response8b

Invalid calendar_type format error (non-alphabetic characters)

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "calendar_type",
      "json_path": "$.fiscal_year.calendar_type",
      "expected_data_type": "text"
    },
    "message": "Please give a valid calendar type",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response9

End month display restriction error for January or February

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "INVALID_DATA",
    "message": "Cannot configure end month as display based option for January and February for custom calendar type",
    "details": {
      "api_name": "display_based_on",
      "json_path": "$.fiscal_year.display_based_on"
    }
  }
}
```

### Status `400` — `application/json` — Error400Response10

Custom fiscal year start year restriction error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "INVALID_DATA",
    "message": "custom fiscal year can be configured only with current year",
    "details": {
      "api_name": "start_date",
      "json_path": "$.fiscal_year.start_date"
    }
  }
}
```

### Status `400` — `application/json` — Error400Response11

Surplus week year out-of-range error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "NOT_ALLOWED",
    "message": "Surplus week can be updated only for current year and next year",
    "details": {
      "api_name": "year",
      "json_path": "$.fiscal_year.surplus_week.year",
      "supported_values": [
        2025,
        2026
      ]
    }
  }
}
```

### Status `400` — `application/json` — Error400Response12

Completed fiscal year surplus week edit error

```json
{
  "fiscal_year": {
    "status": "error",
    "code": "NOT_ALLOWED",
    "message": "Cannot edit surplus week for completed fiscal year",
    "details": {
      "api_name": "year",
      "json_path": "$.fiscal_year.surplus_week.year"
    }
  }
}
```

### Status `400` — `application/json` — AmbiguityStructure

Ambiguity error — calendar_type gregorian sent with structure

```json
{
  "fiscal_year": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "calendar_type",
          "json_path": "$.fiscal_year.calendar_type"
        },
        {
          "api_name": "structure",
          "json_path": "$.fiscal_year.structure"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — AmbiguityStartDate

Ambiguity error — calendar_type gregorian sent with start_date

```json
{
  "fiscal_year": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "calendar_type",
          "json_path": "$.fiscal_year.calendar_type"
        },
        {
          "api_name": "start_date",
          "json_path": "$.fiscal_year.start_date"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — AmbiguityIntervalDisplayOption

Ambiguity error — calendar_type gregorian sent with interval_display_option

```json
{
  "fiscal_year": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "calendar_type",
          "json_path": "$.fiscal_year.calendar_type"
        },
        {
          "api_name": "interval_display_option",
          "json_path": "$.fiscal_year.interval_display_option"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — AmbiguitySurplusWeek

Ambiguity error — calendar_type gregorian sent with surplus_week

```json
{
  "fiscal_year": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "calendar_type",
          "json_path": "$.fiscal_year.calendar_type"
        },
        {
          "api_name": "surplus_week",
          "json_path": "$.fiscal_year.surplus_week"
        }
      ]
    },
    "message": "Ambiguity while processing",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response13

Structure not allowed for gregorian calendar error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "structure",
      "json_path": "$.fiscal_year.structure"
    },
    "message": "cannot configure structure for gregorian calendar",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response14

interval_display_option not allowed for gregorian calendar error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "interval_display_option",
      "json_path": "$.fiscal_year.interval_display_option"
    },
    "message": "cannot configure interval_display_option for gregorian calendar",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response15

surplus_week not allowed for gregorian calendar error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "surplus_week",
      "json_path": "$.fiscal_year.surplus_week"
    },
    "message": "cannot configure surplus week for gregorian calendar",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response16

start_date not allowed for gregorian calendar error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "start_date",
      "json_path": "$.fiscal_year.start_date"
    },
    "message": "cannot configure start_date for gregorian calendar",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response17

Invalid start_month for the configured start_date error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "api_name": "start_month",
      "json_path": "$.fiscal_year.start_month"
    },
    "message": "Invalid start_month for the start_date configured",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response18

Delete surplus week for completed fiscal year error

```json
{
  "fiscal_year": {
    "code": "NOT_ALLOWED",
    "details": {
      "api_name": "year",
      "json_path": "$.fiscal_year.surplus_week.year"
    },
    "message": "Cannot delete surplus week for completed fiscal year",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response19

Missing year in surplus_week error

```json
{
  "fiscal_year": {
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "surplus_week",
        "json_path": "$.fiscal_year.surplus_week"
      },
      "api_name": "year",
      "json_path": "$.fiscal_year.surplus_week.year"
    },
    "message": "Provide valid year for surplus week",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response20

Missing quarter in surplus_week error

```json
{
  "fiscal_year": {
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "surplus_week",
        "json_path": "$.fiscal_year.surplus_week"
      },
      "api_name": "quarter",
      "json_path": "$.fiscal_year.surplus_week.quarter"
    },
    "message": "Provide valid quarter for surplus week",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response21

Missing period in surplus_week error

```json
{
  "fiscal_year": {
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "surplus_week",
        "json_path": "$.fiscal_year.surplus_week"
      },
      "api_name": "period",
      "json_path": "$.fiscal_year.surplus_week.period"
    },
    "message": "Provide valid period for surplus week",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response22

Invalid quarter value in surplus_week error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "json_path": "$.fiscal_year.surplus_week.quarter",
      "supported_values": [
        1,
        2,
        3,
        4
      ]
    },
    "message": "Provide valid quarter for surplus week",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response23

Invalid period value in surplus_week error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {
      "json_path": "$.fiscal_year.surplus_week.period",
      "supported_values": [
        1,
        2,
        3
      ]
    },
    "message": "Provide valid period for surplus week",
    "status": "error"
  }
}
```

### Status `400` — `application/json` — Error400Response24

All fiscal year fields missing error

```json
{
  "fiscal_year": {
    "code": "INVALID_DATA",
    "details": {},
    "message": "Please give a valid data",
    "status": "error"
  }
}
```

### Status `401` — `application/json` — ScopeMismatch

OAuth scope mismatch error

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailed

Authentication failure error

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

Non-admin user attempted to update fiscal year settings

```json
{
  "fiscal_year": {
    "code": "NO_PERMISSION",
    "details": {},
    "message": "Only Admin Users can modify the fiscal year settings",
    "status": "error"
  }
}
```
