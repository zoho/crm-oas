# Examples: createServicesS

**POST /Services__s**

## Request examples

### `application/json` — SamplePostRequest

Successful creation of a service with specific-day availability and job-sheet configuration

```json
{
  "data": [
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": null,
      "Available_From": null,
      "Location": "Client Address",
      "Service_Name": "firstService",
      "Duration": 60,
      "Availability_Type": "Every Business Days",
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Price": 434,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": "2026-01-16",
      "Available_From": "2026-01-10",
      "Availability_Type": "Specific Date Range",
      "Location": "Business Address and Client Address",
      "Service_Name": "secondService",
      "Duration": 30,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Price": 343,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": null,
      "Available_From": null,
      "Location": "Client Address",
      "Service_Name": "thirdService",
      "Duration": 30,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Availability_Type": "Specific Date(s)",
      "Available_Dates": [
        "2026-01-13",
        "2026-01-14",
        "2026-01-15"
      ],
      "Available_Timings": [
        {
          "From": "01:00",
          "To": "04:00"
        },
        {
          "From": "06:00",
          "To": "08:00"
        }
      ],
      "Price": 666,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": null,
      "Available_From": null,
      "Location": "Business Address",
      "Availability_Type": "Specific Day(s)",
      "Service_Name": "fourthService",
      "Duration": 30,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Available_Days": [
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "Price": 3848,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Job_Sheet_Required": "Yes",
      "Available_Till": "2026-01-22",
      "Available_From": "2026-01-02",
      "Availability_Type": "Specific Date Range",
      "Location": "Business Address",
      "Service_Name": "fifthService",
      "Duration": 60,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Available_Timings": [
        {
          "From": "00:00",
          "To": "06:00"
        },
        {
          "From": "07:00",
          "To": "14:00"
        }
      ],
      "Price": 777,
      "Tax": [
        {
          "id": null,
          "value": "Sales Tax - 0.0 %"
        },
        {
          "id": null,
          "value": "Vat - 0.0 %"
        }
      ],
      "Description": "service description",
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    }
  ],
  "skip_mandatory": false
}
```

## Response examples

### Status `201` — `application/json` — Success201

Successful single-record service creation returning a 201 with new record ID and audit metadata.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-12T11:03:03+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-12T11:03:03+04:00",
        "id": "111115000000121665",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record added",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-12T11:25:46+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-12T11:25:46+04:00",
        "id": "111115000000121687",
        "Created_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        }
      },
      "message": "record added",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial batch success with one record created and one rejected due to an invalid Duration value.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "generated_id_0"
      },
      "message": "Proper success message",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "data",
        "json_path": "$.data[0].data"
      },
      "message": "Mandatory field data not found",
      "status": "error",
      "error_meta": "mandatory_missing"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Availability_Type value rejected as not a valid picklist entry.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Availability_Type",
        "json_path": "$.data[0].Availability_Type"
      },
      "message": "The given Availability Type is not in picklist",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

Dependent mismatch error when Available_Days conflict with business days.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Available_Days",
        "json_path": "$.data[0].Available_Days"
      },
      "message": "The given Available Days are not there in business days",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

Dependent mismatch where Available_Timings value does not satisfy business timing constraints.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "To",
        "json_path": "$.data[0].Available_Timings[0].To"
      },
      "message": "Service available time does not satisfy the business timing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Available_Dates contains a value in an invalid date format.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "date",
        "api_name": "Available_Dates",
        "json_path": "$.data[0].Available_Dates"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Invalid data when duration value is outside allowed range.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration value should not be greater than 24hrs or less than 5mins",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Not allowed when job sheets not configured in service preferences.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Job_Sheet_Required",
        "json_path": "$.data[0].Job_Sheet_Required"
      },
      "message": "Job Sheet is not configured in services preferences",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse3

Dependent mismatch where Duration does not fit within the configured service timing window.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration does not satisfy the service timing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Mandatory not found when required Members field is missing

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "Members",
        "json_path": "$.data[0].Members"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

DEPENDENT_FIELD_MISSING error when Available_From is omitted despite Availability_Type being set.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_From",
        "json_path": "$.data[0].Unavailable_From"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Invalid data when Unavailable_From time is outside service availability.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Unavailable_From",
        "json_path": "$.data[0].Unavailable_From"
      },
      "message": "Unavailable From time does not fall within service availability",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse1

Limit exceeded when Members array exceeds 100-user maximum.

```json
{
  "data": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "Members",
        "limit": 100,
        "json_path": "$.data[0].Members"
      },
      "message": "More than 100 users cannot be associated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededResponse2

Limit exceeded when organization has reached 500 active services.

```json
{
  "data": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "Status",
        "limit": 3,
        "json_path": "$.data[0].Status"
      },
      "message": "You cannot create more than 500 active services",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse7

Dependent mismatch where Job_Sheet_Section__s is set but Job_Sheet_Required is No.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Job_Sheet_Required",
          "json_path": "$.data[0].Job_Sheet_Required"
        },
        "api_name": "Job_Sheet_Section__s",
        "json_path": "$.data[0].Job_Sheet_Section__s"
      },
      "message": "Job_Sheet_Section__s can have value only when value of Job_Sheet_Required is Yes",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse8

Dependent mismatch where the Available_Timings To value is not greater than the From value.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Available_Till",
        "json_path": "$.data[0].Available_Till"
      },
      "message": "To value must be Greater than From value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse9

Dependent mismatch where Available_Dates includes a holiday or non-business day.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Available_Dates",
        "json_path": "$.data[0].Available_Dates"
      },
      "message": "Available Dates value in holiday or Not in BusinessDays",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Invalid data when custom time value in Available_Timings is invalid.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "To",
        "json_path": "$.data[0].Available_Timings"
      },
      "message": " The given custom time is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Invalid data when member has not confirmed their account.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "user_status": "unconfirmed",
        "api_name": "id",
        "json_path": "$.data[0].Members[0].Members.id"
      },
      "message": "Members is not Confirmed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Invalid data when member is inactive.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "user_status": "inactive",
        "api_name": "id",
        "json_path": "$.data[0].Members[0].Members.id"
      },
      "message": "Members is not Active",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Invalid data when Owner field received wrong data type.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Owner",
        "expected_data_type": "jsonobject",
        "json_path": "$.data[*].Owner"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Owner field value exceeds the maximum allowed field length.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Owner",
        "maximum_length": 1,
        "json_path": "$.data[*].Owner"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Mandatory not found when required Location field is missing.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "Location",
        "json_path": "$.data[*].Location"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse10

Dependent mismatch when Unavailable_From is invalid for Available status.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_From",
          "json_path": "$.data[0].Unavailable_From"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "When the service status is available, Unavailable From must be greater than current date",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse11

Dependent mismatch error when Unavailable_Till is not a future datetime.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Unavailable Till must be greater than current Time.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse12

Dependent mismatch when both unavailability fields are set for Available status.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_Till",
          "json_path": "$.data[0].Unavailable_Till"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "When the service status is available,  either both Unavailable From and Unavailable Till must be null, or only Unavailable From can have a value.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse13

Dependent mismatch where Unavailable_Till is not earlier than Unavailable_From.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_From",
          "json_path": "$.data[0].Unavailable_From"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Unavailable Till must be lesser than Unavailable From",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse14

Dependent mismatch when Not In Use status conflicts with a future Unavailable_From date.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_From",
          "json_path": "$.data[0].Unavailable_From"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Services status cannot be marked as Not In Use when Unavailable From falls after the current Date",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse15

Dependent mismatch when Available_From precedes the current date.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Starting date of service availability falls before the current Date, so service cannot be marked as Scheduled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse16

Dependent mismatch when a past Available_Till conflicts with an active service status.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_Till",
          "json_path": "$.data[0].Available_Till"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "End Date of service availability falls before the current Date, so service cannot be marked as Available or Scheduled or Temporarily Unavailable",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Unavailable_From time falls outside the service availability window.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Unavailable_From",
        "json_path": "$.data[0].Unavailable_From"
      },
      "message": "Unavailable From time does not fall within service availability",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

Dependent field missing error when Unavailable_From is absent for Status.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Invalid data error returned with no specific error code in the payload.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "data",
    "json_path": "$.data"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Status field rejected due to incorrect data type instead of expected text.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Status",
        "expected_data_type": "text",
        "json_path": "$.data[*].Status"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Status value exceeds maximum allowed length.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Status",
        "maximum_length": 120,
        "json_path": "$.data[*].Status"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Unavailable_Till contains an unsupported picklist value.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Unavailable_Till",
        "supported_values": [
          "Temporarily Unavailable",
          "Available",
          "Not In Use",
          "Scheduled"
        ],
        "json_path": "$.data[*].Unavailable_Till"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Job_Sheet_Required receives an invalid data type.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "Job_Sheet_Required",
        "expected_data_type": "text",
        "json_path": "$.data[*].Job_Sheet_Required"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Job_Sheet_Required value exceeds the maximum allowed length.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "Job_Sheet_Required",
        "maximum_length": 3,
        "json_path": "$.data[*].Job_Sheet_Required"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse17

Dependent mismatch when a scheduled service is set to Not In Use or Temporarily Unavailable.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Available_From",
          "json_path": "$.data[0].Available_From"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Service status cannot be marked as Not In Use or Temporarily Unavailable for scheduled services.",
      "status": "error"
    }
  ]
}
```
