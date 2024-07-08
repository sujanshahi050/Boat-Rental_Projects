import BoatRentalClass as BRC

class Project:

    def run(self):

        rental_options = {
            "show_boats_table": "Shows boats table!",
            "show_rentals": "Shows rental table",
            "show_customers": "Shows customer table",
            "exit": "Exit the program"
        }
        print("Welcome to the boat rental inventory program, please choose a selection")

        user_selection = ""
        while user_selection != "exit":
            print("*** Option List ***")
            for option in rental_options.items():
                print(option)
            
            user_selection = input("Select an option: ").lower()
            boat_rental_class = BRC.BoatRental("boat_rental.sqlite")

            if user_selection == "show_boats_table":
                results = boat_rental_class.fetch_boat_inv()
                for item in results:
                    print(item)
                input("Press return to continue")

            elif user_selection == "show_rentals":
                results = boat_rental_class.fetch_rental_inv()
                for item in results:
                    print(item)
                input("Press return to continue")
            elif user_selection == "show_customers":
                pass
                #TODO: Implement fetch_customer_data on BoatRentalClass
            
            else:
                if user_selection != "exit":
                    print("Invalid selection, try again")


project = Project()
project.run()