import json

class VisaApplicationSystem:
    def __init__(self, filename):
        self.filename = filename
        self.applications = self.load_applications()

    def load_applications(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data['store']
        except FileNotFoundError:
            return []

    def save_applications(self):
        data = {'store': self.applications}
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def create_application(self, passport_number, application_id, status_id, from_country, to_country):
        application = {
            'passport_number': passport_number,
            'application_id': application_id,
            'status_id': status_id,
            'from_country': from_country,
            'to_country': to_country
        }
        self.applications.append(application)
        self.save_applications()
        print("Application created successfully.")

    def read_application(self, application_id):
        for application in self.applications:
            if application['application_id'] == application_id:
                print("Application Details:")
                print(application)
                return
        print("Application not found.")

    def update_application(self, application_id, **kwargs):
        for application in self.applications:
            if application['application_id'] == application_id:
                for key, value in kwargs.items():
                    application[key] = value
                self.save_applications()
                print("Application updated successfully.")
                return
        print("Application not found.")

    def delete_application(self, application_id):
        for i, application in enumerate(self.applications):
            if application['application_id'] == application_id:
                del self.applications[i]
                self.save_applications()
                print("Application deleted successfully.")
                return
        print("Application not found.")

    def process_visa_application(self, application_id):
        for application in self.applications:
            if application['application_id'] == application_id:
                application['status_id'] = "Processed"
                self.save_applications()
                print(f"Visa application {application_id} processed successfully.")
                return
        print("Application not found.")

    def track_application_status(self, status_id):
        status_applications = [app for app in self.applications if app['status_id'] == status_id]
        if status_applications:
            print(f"Applications with status '{status_id}':")
            for application in status_applications:
                print(application)
        else:
            print("No applications found with this status.")


def main():
    visa_system = VisaApplicationSystem("visa_applications.json")

    while True:
        print("\nMenu:")
        print("1. Create Visa Application")
        print("2. Read Visa Application")
        print("3. Update Visa Application")
        print("4. Delete Visa Application")
        print("5. Process Visa Application")
        print("6. Track Application Status")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            passport_number = input("Enter passport number: ")
            application_id = input("Enter application ID: ")
            status_id = input("Enter status ID: ")
            from_country = input("Enter from country: ")
            to_country = input("Enter to country: ")
            visa_system.create_application(passport_number, application_id, status_id, from_country, to_country)

        elif choice == "2":
            application_id = input("Enter application ID to read: ")
            visa_system.read_application(application_id)

        elif choice == "3":
            application_id = input("Enter application ID to update: ")
            field = input("Enter field to update (passport_number, status_id, from_country, to_country): ")
            value = input(f"Enter new value for {field}: ")
            visa_system.update_application(application_id, **{field: value})

        elif choice == "4":
            application_id = input("Enter application ID to delete: ")
            visa_system.delete_application(application_id)

        elif choice == "5":
            application_id = input("Enter application ID to process: ")
            visa_system.process_visa_application(application_id)

        elif choice == "6":
            status_id = input("Enter status to track: ")
            visa_system.track_application_status(status_id)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
