class Carshowroom:
    def init(self):
        self.company_name = ""
        self.model_name = ""
        self.showroom_price=""

    def Company(self, company_name):
        
            self.company_name = company_name
            print("Welcome to", self.company_name, "company")

    def Model(self):
            if self.company_name == "Hyundai":
                 models = ["Creta", "Venue", "I20"]

            elif self.company_name == "Renault":
                 models = ["Kwid", "Triber", "kiger"]
            
            elif self.company_name == "MG":
                 models = ["ZS EV", "Astor", "Comet EV"]
                
                
            else:
               print("Invalid company name")
               return
            print("Models available for", self.company_name, ":", models)  
            self.model_name = input("Select a model: ")

    def Price(self):
        if self.company_name=="Hyundai" and self.model_name=="Creta":
            self.showroom_price=25000
        elif self.company_name=="Hyundai" and self.model_name=="Venue":
            self.showroom_price=26000
        elif self.company_name=="Hyundai" and self.model_name=="I20":
             self.showroom_price=31000
        elif self.company_name=="Renault" and self.model_name=="Kwid":
            self.showroom_price=27000
        elif self.company_name=="Renault" and self.model_name=="Triber":
            self.showroom_price=28000
        elif self.company_name=="Renault" and self.model_name=="Kiger":
             self.showroom_price=32000
        elif self.company_name=="MG"and self.model_name=="ZS EV":
            self.showroom_price=29000
        elif self.company_name=="MG" and self.model_name=="Astor":
            self.showroom_price=30000
        elif self.company_name=="MG" and self.model_name=="comet EV":
             self.showroom_price=33000
        else:
            print("invalid")
            return
        gst_tax = 0.05 * self.showroom_price
        cgst_tax = 0.05 * self.showroom_price
        road_price = self.showroom_price + gst_tax + cgst_tax
        print("Road price for", self.company_name, self.model_name, "is:", road_price)

car_showroom = Carshowroom()
comp = input("Enter Company Name")
car_showroom.Company(comp)
car_showroom.Model()
car_showroom.Price()
