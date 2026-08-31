# Deal Link Emails

- [OpenAPI specification](deal_link_emails.yaml)
- [Link Emails to Deals](operations/linkEmailsToDeals/operation.md)
  - To link a deal with one or more of a contact's emails. An email can only be linked to a single deal at a time. Zoho CRM automatically links a contact's incoming emails to the deals using the [Deal Prediction Mechanism](https://help.zoho.com/portal/en/kb/crm/connect-with-customers/email/user-functions/articles/email-association-with-deal#Auto-link_Emails_by_Deal_Prediction_Mechanism). You can also manage these links using the Link Deal to Emails API and [Unlink Deal from Emails API](deal_link_emails.yaml#$.paths./Contacts/{contactId}/Emails/{messageId}/actions/link_record.delete).
  - [Examples](operations/linkEmailsToDeals/examples/)
- [Unlink Emails from Deals](operations/unlinkEmailsFromDeal/operation.md)
  - To unlink deals from one or more of a contact's emails. An email will only be linked to a single deal at a time. When you call this API, the specified email(s) will be unlinked from them. The user's profile requires "View" permission for Deals and Contacts modules to use this API.
  - [Examples](operations/unlinkEmailsFromDeal/examples/)
- [Link Deal Email](operations/linkEmailToRecord/operation.md)
  - Links an email to a specified record in CRM.
  - [Examples](operations/linkEmailToRecord/examples/)
- [Unlink Deal Email](operations/unlinkEmailFromRecord/operation.md)
  - Unlinks an email from a specified record in CRM.
  - [Examples](operations/unlinkEmailFromRecord/examples/)
