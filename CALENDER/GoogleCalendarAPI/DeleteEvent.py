## Script to delete events from google calendar

    from cal_setup import get_calendar_service

    def main():
       # Delete the event
       service = get_calendar_service()
       try:
           service.events().delete(
               calendarId='primary',
               eventId='<place your event ID here>',
           ).execute()
       except googleapiclient.errors.HttpError:
           print("Failed to delete event")

       print("Event deleted")

    if __name__ == '__main__':
       main()
