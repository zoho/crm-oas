# Record Email Sharing

- [OpenAPI specification](record_share_email.yaml)
- [Share Record Emails](mds/shareEmails.md)
  - To share email threads linked to a specific CRM record with colleagues in the same organization. Requires custom email sharing to be enabled in the organization and a valid email configuration for the user.
  - [Examples](mds/examples/shareEmails.md)
- [Unshare Record Emails](mds/unshareEmails.md)
  - To revoke email sharing for a specific CRM record, making the linked email threads no longer visible to colleagues. Requires custom email sharing to be enabled in the organization and a valid email configuration for the user.
  - [Examples](mds/examples/unshareEmails.md)
- [Share Record Emails](mds/shareBulkEmails.md)
  - To share email threads linked to multiple CRM records with colleagues in the same organization. Accepts up to 100 record IDs per request. Supports partial success - each record in the response is processed independently, and individual results indicate success or failure.
  - [Examples](mds/examples/shareBulkEmails.md)
- [Unshare emails in bulk](mds/unshareBulkEmails.md)
  - To revoke email sharing for multiple CRM records in a single request. Accepts up to 100 record IDs per request. The `data` array in the 207 response contains an item for each record, indicating success or failure.
  - [Examples](mds/examples/unshareBulkEmails.md)
