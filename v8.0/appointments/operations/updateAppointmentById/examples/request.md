### `application/json` — SamplePutRequest

PUT request body with a data array for a single appointment record update

```json
{
  "data": [
    {
      "Appointment_Name": "service06 - ll",
      "Appointment_For": {
        "module": {
          "api_name": "Contacts",
          "id": "111115000000002654"
        },
        "name": "ll",
        "id": "111115000000120725"
      },
      "Service_Name": {
        "name": "service06",
        "id": "111115000000127506"
      },
      "Appointment_Start_Time": "2026-01-16T18:00:00+05:30",
      "Location": "Business Address",
      "Address": null,
      "Owner": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Additional_Information": null,
      "Remind_At": [
        {
          "unit": 1,
          "period": "hours"
        }
      ],
      "Created_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Modified_By": {
        "name": "madesh04",
        "id": "111115000000058229",
        "email": "madeshwaran.g+csez04@zohotest.com"
      },
      "Created_Time": "2026-01-16T16:50:29+05:30",
      "Modified_Time": "2026-01-19T16:12:24+05:30",
      "Tag": [],
      "Status": "Overdue",
      "Last_Activity_Time": "2026-01-19T16:12:24+05:30",
      "Rescheduled_From": null,
      "Reschedule_Reason": null,
      "Reschedule_Note": null,
      "Rescheduled_By": null,
      "Rescheduled_Time": null,
      "Cancelled_By": null,
      "Cancellation_Reason": null,
      "Cancellation_Note": null,
      "Job_Sheet_Created__s": false,
      "Cancelled_Time": null,
      "Job_Sheet_Name__s": null,
      "Job_Sheet_Description__s": null,
      "Date_1": null,
      "Reschedule_Count": 0,
      "Appointment_End_Time": "2026-01-16T18:30:00+05:30",
      "Duration": 30,
      "Rescheduled_To": null
    }
  ]
}
```
