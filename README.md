**Application Title: pressure-QR-code-converter**

**Overview:**

The application is made up of three screens and 4 routes. The main ouput of this application allows Employees to LOAD pressure readings, View presuure readings, Upload preassure readings and 
Generate QR codes containing the pressure data.

**Requirements:**

The application requirements are as follows:

- Django and Python environment needs to be properly setup.
- Requirements.txt file needs to run and all libraries installed.
- Preferably ran in a Chrome window browser.

**Project Structure:**
root/
  - data/
  - media/
  - my_app/
      - templates/
        - my_app/
           - capture_pressure.html
           - home.html
           - imports.html
      - __init__.py
      - admin.py
      - apps.py
      - forms.py
      - models.py
      - tests.py
      - views.py
  - config/
      - __init__.py
      - asgi.py
      - settings.py
      - urls.py
      - wsgi.py
  - manage.py

The above is the required structure for running the appplication.

**Note - I tried to organize the strucure according to the project request but the program broke when I moved it. It was an oversight on my end by not starting with the instructed structure. Hence providing the above structure to ensure all works accordingly.

**Application Usage guide:**

**OnRun():**
- On launch of the application you should land on the home route i.e the Home Page.
- You should see information text on the Hoome Page and a Nav Bar with options to navigate Home, Capturing Pressure and Importing pressure data.
- No Table Data will be displayed as pressure uploads or creation are required before displaying the data.

**Navigation():**
- Three page routes are available. Home, Capture Pressure and Import.
  
- **Capture Pressure Page:**
  ![image](https://github.com/user-attachments/assets/7fd7b061-3611-471a-a5f3-e0884cfa2b65)

  - The page should Display the heading and display fields to capture new pressure data. The capure fields are what I could depict from the Delphi codebase.
  - Each field is required before the form can be saved.
  - A dismissable flash message should appear if submit button is clicked and required fields have not been filled.
  - Complete the fields, note, the Capture Date has a calendar widget and should display the calendar when selecting the date.
  - On successful submission a dismissable flash meesage should indicate the upload/creation was successful.
  - Navigate back to the Home Page, the uploaded record should display in the table, grouped by Sample Number.
  
- **Home**
  ![image](https://github.com/user-attachments/assets/76adb97c-1434-4cbc-94d8-0719b4748c16)

  - The Home Page will display the created record in a table format. All the captured form fields should display in a row and grouped by the sample number.
  - Adding multiple records with the same Sample Number should be displayed grouped as mentioned above.
  - The QR Code Column shoudl by default display 'No QR COde Generated'.
  - If the Generate QR button is clicked it should show an alert indicating successful geenration and reload instruction and after reload display the generated QR code.

    
  



