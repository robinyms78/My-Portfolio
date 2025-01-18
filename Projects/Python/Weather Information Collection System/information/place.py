# Get zip code from address in qubic server
#current_location = information.qubic.get_store_information()['address']
#current_place = place.Place(current_location)
#current_location = '102-0093, jp'


class Place:
    # Initialize by zip code
    def __init__(self, zipcode):
        """
        :param address: currently address is a zip code ex: 999-9999, jp
        """
        self.zipcode = zipcode

    # Get zip code
    def get_zip_code(self):
        # Read zipcode from text file
        with open("information/zip.csv", "r") as myfile:
            self.zipcode = myfile.readlines()[0]
            print("Received zipcode: ", self.zipcode + ",jp")
        return str(self.zipcode) + ",jp"

