import pandas as pd


class FoodInspections: 
    """An inspection of food going through the system.
    """
    def __init(self, "establishments.csv", "food_inspections.csv"):
        """"Read files into dataframe.

        Attributes:
            inspections(str): Representing a merged dataframe 
        """
        establishment = pd.read_csv(self.establishments)
        food = pd.read_csv(self.food_inspections)
        
        inspections = pd.merge(establishment, food, how= "left", on= "Establishment_id")
             
    def analyze(self, distance):
        """Calls the filter method.

        Attributes:
            distance(float): Representing the distance to McKeldin.
        """
        df = self.filter(distance)
        counts = df.groupby("Establishment_id")["Establishment_id"].count()
        violator_ids = counts[counts == counts.max()]
        v = pd.merge(violator_ids, df, how="left", left_index=True,
                     right_on="Establishment_id") ["Name"].unique()
        return v.tolist(), counts.max()
           
    def filter(self, distance):
        """Applies a filter to the inspections df keeping the rows for which the condition is met.

        Attributes:
            distance(float): Representing the distance to McKeldin.
        """
        self.inspections.filter("Distance_to_Mckeldin")
        self.inspections[(inspections["Inspection_type"] == "Monitoring") or 

        (inspections["Inspection_type"]=='Comprehensive')]

        self.inspections[(inspections["Inspection_results"] == "Critical Violations observed")
  

        return inspections
               
def main("establishments.csv", "food_inspections.csv", distance):
    """Instantiates a FoodInspection object passing in the paths of both objects,
       Calls the object's analyze() method,
       Prints a message indicating the names of establishments withn the most violations.   
    """
    results = FoodInspections("establishments.csv", "food_inspections.csv")

    results.analyze(distance)

    z = zip(x['Name']

    done = tuple(z)

    print(done)
    
    
    
if __name__ == '__main__': 
    main()
