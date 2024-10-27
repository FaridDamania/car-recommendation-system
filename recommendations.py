import csv
import os

def recommend(family_members, budget, fuel_type):
    recommendations = []
    csv_file_path = 'data1_clean.csv'

    if not os.path.exists(csv_file_path):
        return [f"Error: {csv_file_path} not found."]

    try:
        with open(csv_file_path, 'r') as fo:
            data = csv.reader(fo, delimiter='|')
            headers = next(data)  # Skip the header

            # Logic to recommend cars based on user input
            for row in data:
                car_price = float(row[8])
                car_seats = int(row[9])
                car_fuel = row[6]

                if (car_price <= float(budget)) and (car_seats >= int(family_members)):
                    if fuel_type == 'Anything' or fuel_type == car_fuel:
                        car_info = f"{row[1]} {row[2]} {row[3]} - Price: {row[8]} L, Mileage: {row[7]} KMPL"
                        recommendations.append(car_info)

        if not recommendations:
            return ["No cars found that match your criteria."]
        return recommendations
    except Exception as e:
        # Log error to terminal for debugging
        print(f"Error processing CSV: {str(e)}")
        return [f"Error: {str(e)}"]
