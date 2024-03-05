# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == MY COMMENTS ==
# Copy all code over from password_manager as a few methods are in there
# Sort service by and get for services aren't - sort and get functions? Also has None in it

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():
    
    def __init__(self):
    
        self.services = {}


    def add(self, service, password):
        
        if self.is_valid(password) and password not in self.services.values():

            self.services[service] = [password, datetime.now()]
        
    def remove(self, service):

        if service in self.services:

            del self.services[service]

    def update(self, service, password):

        if self.is_valid(password):

            [_, added_on] = self.services[service]

            self.services[service] = [password, added_on]

    def get_for_service(self, service):

        password = self.services.get(service, None)

        if password is None:
            return
        else:
            return password[0]

    def list_services(self):

        return list(self.services.keys())

    def sort_services_by(self, added_on, reverse=False):
        if added_on == 'service':
            
            sorted_services = sorted(self.services.keys())

        elif added_on == 'added_on':
            date_dict = {}
            for (service, value) in self.services.items():
                added_on = value[1]
                date_dict[added_on] = service
            dates_added = list(date_dict.keys())
            dates_added.sort()
            sorted_services = []
            for date in dates_added:
                sorted_services.append(date_dict[date]) 

        if reverse:
            sorted_services.reverse()

        return sorted_services

        
    def is_valid(self, password):

        list_of_passwords = [password[0] for password in self.services.values()]

        if password in list_of_passwords:
            return False

        if len(password) < 8:
            return False

        spec_char = ['!', '@', '$', '%', '&']
        for char in spec_char:
            if char in password:
                return True


        
        

    


