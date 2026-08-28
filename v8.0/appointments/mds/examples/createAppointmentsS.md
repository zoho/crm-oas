# Examples: createAppointmentsS

**POST /Appointments__s**

## Request examples

### `application/json` — SamplePostRequest

Request body with four appointment objects covering varied statuses.

```json
{
  "data": [
    {
      "Status": "Scheduled",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Service_Name": {
        "name": "service04",
        "id": "111115000000127440"
      },
      "Appointment_Start_Time": "2026-01-29T12:00:00+04:00",
      "Appointment_End_Time": "2026-01-29T12:30:00+04:00",
      "Duration": 30,
      "Appointment_Name": "service04 - bb",
      "Location": "Business Address",
      "Address": null,
      "Owner": {
        "id": "111115000000122075",
        "email": "madeshwaran.g+csez02@zohotest.com",
        "name": "madesh"
      },
      "Additional_Information": null,
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "$currency_symbol": "£",
      "$sharing_permission": "full_access",
      "$state": "save",
      "$editable": true,
      "Tag": [],
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Created_Time": "2026-01-16T09:39:43+04:00",
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Modified_Time": "2026-01-16T09:39:43+04:00",
      "Rescheduled_From": null,
      "Rescheduled_To": null,
      "Reschedule_Reason": null,
      "Rescheduled_Time": null,
      "Reschedule_Count": 0,
      "Rescheduled_By": null,
      "Reschedule_Note": null,
      "Cancellation_Reason": null,
      "Cancellation_Note": null,
      "Cancelled_By": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Record_Status__s": "Available"
    },
    {
      "Owner": {
        "id": "111115000000122075",
        "email": "madeshwaran.g+csez02@zohotest.com",
        "name": "madesh"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-22T13:00:00+04:00",
      "Cancellation_Reason": null,
      "$field_states": null,
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": "2026-01-22T13:00:00+04:00",
      "$sharing_permission": "full_access",
      "Reschedule_Reason": "By Customer",
      "Additional_Information": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Cancellation_Note": null,
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 2,
      "Rescheduled_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Date_1": "2026-01-14",
      "Rescheduled_Time": "2026-01-16T10:29:58+04:00",
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "Appointment_End_Time": "2026-01-22T13:30:00+04:00",
      "Status": "Scheduled",
      "Modified_Time": "2026-01-16T10:29:58+04:00",
      "Service_Name": {
        "name": "service04",
        "id": "111115000000127440"
      },
      "Created_Time": "2026-01-16T09:39:43+04:00",
      "Rescheduled_From": "2026-01-21T14:30:00+04:00",
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "service-reschedule",
      "Duration": 30,
      "Record_Status__s": "Available",
      "$status": "cmv_1-1",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": "for customer need"
    },
    {
      "Owner": {
        "id": "111115000000122075",
        "email": "madeshwaran.g+csez02@zohotest.com",
        "name": "madesh"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-22T13:00:00+04:00",
      "Cancellation_Reason": "By Customer",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": "2026-01-22T13:00:00+04:00",
      "$sharing_permission": "full_access",
      "Reschedule_Reason": "By Customer",
      "Additional_Information": null,
      "Last_Activity_Time": "2026-01-16T10:34:44+04:00",
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": "2026-01-16T10:34:44+04:00",
      "Cancellation_Note": "request from customer",
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 2,
      "Rescheduled_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Date_1": "2026-01-14",
      "Rescheduled_Time": "2026-01-16T10:29:58+04:00",
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "Appointment_End_Time": "2026-01-22T13:30:00+04:00",
      "Status": "Cancelled",
      "Modified_Time": "2026-01-16T10:34:44+04:00",
      "Service_Name": {
        "name": "service04",
        "id": "111115000000127440"
      },
      "Created_Time": "2026-01-16T09:39:43+04:00",
      "Rescheduled_From": "2026-01-21T14:30:00+04:00",
      "Cancelled_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "$editable": true,
      "Appointment_Name": "service04 - bb",
      "Duration": 30,
      "Record_Status__s": "Available",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": "for customer need"
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com",
        "name": "madesh04"
      },
      "$currency_symbol": "£",
      "Address": null,
      "Appointment_Start_Time": "2026-01-07T13:00:00+04:00",
      "Cancellation_Reason": null,
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "bb",
        "id": "111115000000120715"
      },
      "Rescheduled_To": null,
      "$sharing_permission": "full_access",
      "Reschedule_Reason": null,
      "Job_Sheet_Name__s": "ss",
      "Additional_Information": null,
      "Last_Activity_Time": null,
      "Job_Sheet_Created__s": true,
      "Cancelled_Time": null,
      "Cancellation_Note": null,
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Reschedule_Count": 0,
      "Rescheduled_By": null,
      "Date_1": null,
      "Rescheduled_Time": null,
      "Remind_At": null,
      "Appointment_End_Time": "2026-01-07T15:00:00+04:00",
      "Status": "Completed",
      "Modified_Time": "2026-01-16T10:40:45+04:00",
      "Service_Name": {
        "name": "service03",
        "id": "111115000000127405"
      },
      "Created_Time": "2026-01-16T10:40:45+04:00",
      "Rescheduled_From": null,
      "Cancelled_By": null,
      "$editable": true,
      "Appointment_Name": "service-jobsheet",
      "Duration": 120,
      "Job_Sheet_Section__s": "Job Sheet Information",
      "Record_Status__s": "Available",
      "Job_Sheet_Description__s": "done and dusted",
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Tag": [],
      "Location": "Business Address",
      "Reschedule_Note": null
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

All four appointment records created successfully.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147145",
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
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147147",
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
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147149",
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
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147151",
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

### Status `201` — `application/json` — Success200

Appointment records created successfully.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147145",
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
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147147",
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
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147149",
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
        "Modified_Time": "2026-01-16T10:52:02+04:00",
        "Modified_By": {
          "name": "madesh04",
          "id": "111115000000058229"
        },
        "Created_Time": "2026-01-16T10:52:02+04:00",
        "id": "111115000000147151",
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

207 with one MANDATORY_NOT_FOUND failure and one success.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "data",
        "json_path": "$.data[0].data"
      },
      "message": "required field not found",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "generated_id_0"
      },
      "message": "Proper success message",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

MANDATORY_NOT_FOUND for missing Appointment_For field.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "Appointment_For",
        "json_path": "$.data[2].Appointment_For"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldUnchangedResponse1

DEPENDENT_FIELD_UNCHANGED for Rescheduled_From equals start time.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_UNCHANGED",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Reschedule_From and Appointment_Start_Time cannot be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

DEPENDENT_FIELD_MISSING when Rescheduled_From is empty.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Reschedule_Reason",
          "json_path": "$.data[0].Reschedule_Reason"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Rescheduled_From cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

NOT_ALLOWED for service unavailable at appointment start time.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Service is not available on the given time",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

NOT_ALLOWED for appointment start time outside business hours.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Appointment time does not falls under business hours",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse1

DEPENDENT_MISMATCH for Owner not in service members.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Services.Members",
          "json_path": "$.data[0].Services.Members"
        },
        "api_name": "id",
        "json_path": "$.data[0].Owner.id"
      },
      "message": "Appointment Owner is not a part of Service Members",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA for Appointment_For module invalid JSON object.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "module",
        "json_path": "$.data[0].Appointment_For.module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

INVALID_DATA for Appointment_For module not in multi-module lookup

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.data[0].Appointment_For.module.api_name"
      },
      "message": "the given module name is not exist in multimodulelookup",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse2

DEPENDENT_FIELD_MISSING for Status not set to Cancelled.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Cancellation_Reason",
          "json_path": "$.data[0].Cancellation_Reason"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "To Update the fields of Cancellation Information Section, value of Status should be Cancelled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse3

NOT_ALLOWED for marking appointment Completed without job sheet.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed without creating the jobsheet",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse2

DEPENDENT_MISMATCH for Status Completed before end time.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as completed before the appointment ends",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse3

DEPENDENT_MISMATCH for job sheet on incomplete appointment.

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
        "api_name": "Job_Sheet_Name__s",
        "json_path": "$.data[0].Job_Sheet_Name__s"
      },
      "message": "Job Sheet can be created only for completed appointment",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse4

DEPENDENT_MISMATCH for Status Overdue before end time.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be marked as overdue before the appointment ends",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse5

DEPENDENT_MISMATCH for appointment scheduled in the past.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be scheduled for past dates",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

MANDATORY_NOT_FOUND for missing unit key in Remind_At.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "mandatory key missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

INVALID_DATA for data array exceeding maximum length.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 4,
    "api_name": "data",
    "json_path": "$.data"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse4

INVALID_DATA invalid type for Remind_At unit field.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit"
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

INVALID_DATA for Remind_At unit value out of allowed range.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "unit",
        "json_path": "$.data[0].Remind_At[0].unit",
        "range": {
          "from": 0,
          "to": 100
        }
      },
      "message": "Please check whether the input values are correct",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchCancellationResponse1

DEPENDENT_MISMATCH for Cancellation_Reason without Status Cancelled.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Cancellation_Reason",
          "json_path": "$.data[0].Cancellation_Reason"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "To Update the fields of Cancellation Information Section, value of Status should be Cancelled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingAddressResponse1

DEPENDENT_FIELD_MISSING for Address when Location is set.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Location",
          "json_path": "$.data[0].Location"
        },
        "api_name": "Address",
        "json_path": "$.data[0].Address"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLengthAddressResponse1

INVALID_DATA max length exceeded for Address.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 255,
        "api_name": "Address",
        "json_path": "$.data[0].Address"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLengthAppointmentNameResponse1

INVALID_DATA max length exceeded for Appointment_Name.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 225,
        "api_name": "Appointment_Name",
        "json_path": "$.data[0].Appointment_Name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLengthAdditionalInformationResponse1

INVALID_DATA max length exceeded for Additional_Information.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 32000,
        "api_name": "Additional_Information",
        "json_path": "$.data[0].Additional_Information"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLengthCancellationNoteResponse1

INVALID_DATA max length exceeded for Cancellation_Note.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 2000,
        "api_name": "Cancellation_Note",
        "json_path": "$.data[0].Cancellation_Note"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLengthRescheduleNoteResponse1

INVALID_DATA max length exceeded for Reschedule_Note.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 2000,
        "api_name": "Reschedule_Note",
        "json_path": "$.data[0].Reschedule_Note"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

INVALID_DATA unsupported value for Remind_At period field.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.data[0].Remind_At[0].period",
        "supported_values": [
          "minutes",
          "hours",
          "days"
        ]
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```
