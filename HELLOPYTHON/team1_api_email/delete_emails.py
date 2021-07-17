from team1_api_email.common import gmail_authenticate, search_messages

def delete_messages(service, query):
    messages_to_delete = search_messages(service, query)
    # it's possible to delete a single message with the delete API, like this:
    # service.users().messages().delete(userId='me', id=msg['id'])
    # but it's also possible to delete all the selected messages with one query, batchDelete
    return service.users().messages().batchDelete(
      userId='me',
      body={
          'ids': [ msg['id'] for msg in messages_to_delete]
      }
    ).execute()

# delete
if __name__ == "__main__":
    service = gmail_authenticate()
    delete_messages(service, "삭제할 메일의 이메일 주소")
    delete_messages(service, "bjh28712745@gmail.com")