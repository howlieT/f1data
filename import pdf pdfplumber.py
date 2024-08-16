import pdfplumber

# Step 1: Extract text from PDF
pdf_path = "Lap Analysis - SIN.pdf"
with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]  # Assuming the lap data is on the first page
    table = page.extract_table()

# Step 2: Identify drivers and initialize the dictionary
drivers = table[0]  # Extract driver names from the first row
driver_lap_times = {}

# Initialize the dictionary with driver names as keys and empty lists as values
for driver in drivers:
    if driver and driver != "":  # Ensure we are not adding empty strings as keys
        driver_lap_times[driver] = []

# Step 3: Populate the dictionary with lap times
for row in table[1:]:  # Skip the first row with driver names
    for i, lap_time in enumerate(row):
        if i < len(drivers):  # Ensure the index is within the range of drivers
            driver = drivers[i]
            if driver and lap_time:  # Check if both driver and lap time are present
                driver_lap_times[driver].append(lap_time)

# Step 4: Print or process the lap times for each driver
for driver, laps in driver_lap_times.items():
    print(f"{driver}: {laps}")