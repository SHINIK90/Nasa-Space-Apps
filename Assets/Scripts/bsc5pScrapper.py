import csv

# Your HR name list (replace with your actual list)
hr_names_list = ['HR 2061','HR 1713','HR 1790','HR 1903','HR 1851','HR 1948','HR 2004','HR 1879','HR 1899','HR 1543','HR 4301','HR 4295','HR 4554','HR 4660','HR 4905','HR 5055','HR 5191','HR 3594','HR 4033','HR 424','HR 5563','HR 5735','HR 6789','HR 6322','HR 21','HR 168','HR 403','HR 264','HR 542','HR 219','HR 321','HR 264','HR 6134','HR 6527','HR 6553','HR 5953','HR 5984','HR 5944','HR 6580','HR 6241','HR 6580','HR 3982','HR 4534','HR 4057','HR 4357','HR 4359','HR 3852','HR 3905','HR 17','HR 1457','HR 1791','HR 1165','HR 1178','HR 1149','HR 1142','HR 1145','HR 1140','HR 1156','HR 7924','HR 7418','HR 7796','HR 7949','HR 7528','HR 2491','HR 2618','HR 2693','HR 2827','HR 2294','HR 2657','HR 2282','HR 2943','HR 2845','HR 2891','HR 2990','HR 2421','HR 2777','HR 2473','HR 2286','HR 2650','HR 6879','HR 7121','HR 7194','HR 6859','HR 6746','HR 7343','HR 7597','HR 7001','HR 7106','HR 7178','HR 7139','HR 7054','HR 936','HR 1017','HR 1131','HR 921','HR 1228','HR 1203','HR 1087','HR 4730','HR 4853','HR 4763','HR 4656','HR 4700','HR 3748','HR 3482','HR 3418','HR 4450','HR 5020','HR 15','HR 337','HR 603','HR 165','HR 154','HR 269','HR 5459','HR 5267','HR 5288','HR 5132',]

# Path to your text file
txt_file_path = r'D:\UnityProjects1Tb\Electric Fields VR\Assets\NASA\Scripts\bsc5p.txt'

# Step 1: Read the raw data from the file
with open(txt_file_path, 'r') as file:
    raw_data = file.read()

# Step 2: Parse the data and filter based on HR names
rows = []
remaining_hr_names = hr_names_list.copy()  # Copy the original list to modify it

for line in raw_data.strip().splitlines():
    line = line.strip('|').split('|')
    if len(line) > 1:  # Only add valid rows
        parsed_row = [col.strip() for col in line]
        # Check if any HR name in the remaining list exists in the row
        for hr_name in remaining_hr_names:
            if hr_name in parsed_row[0]:  # Check the first column (HR name)
                rows.append(parsed_row)  # Add the row to the results
                remaining_hr_names.remove(hr_name)  # Remove the HR name from the list
                break  # No need to check other HR names for this row

# Step 3: Sort based on the order of hr_names_list
sorted_rows = [row for hr in hr_names_list for row in rows if hr in row[0]]

# Step 4: Output as CSV
csv_filename = 'filtered_hr_data.csv'
header = ['name', 'alt_name', 'ra', 'dec', 'vmag', 'bv_color', 'hr', 'parallax', 'ub_color']

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(sorted_rows)  # Write the sorted rows

print(f"CSV file '{csv_filename}' has been created successfully.")