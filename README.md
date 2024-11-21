**Application Title: pressure-QR-code-converter**

**Overview:**

The application is made up of three screens and 4 routes. The main ouput of this application allows Employees to LOAD pressure readings, View pressure readings, Upload pressure readings and 
Generate QR codes containing the pressure data.

**Requirements:**

The application requirements are as follows:

- Django and Python environment needs to be properly setup.
- Requirements.txt file needs to run and all libraries installed.
- Preferably ran in a Chrome window browser.
  
_**---21/11/2024---

** Note from Rayn:
  I noticed this morning the clone will give some errors when trying to run the project, reason for this i moved the folders to the scr folder i tried to create at the end but like mentioned 
  below it broke the program. The below will resolve the issues:**_

  - Python interpreter : 3.10
  - Imports are pointing to 'src.' this should be removed and only reference 'my_app'.
  - Changes requried:
    -  example => 'from src.my_app import' solution => 'src.' should be removed as the directory is deleted
  - I can push the amendments as well, if required, to the files.
      
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
  - The QR Code Column should by default display 'No QR COde Generated'.
  - If the Generate QR button is clicked it should show an alert indicating successful geenration and reload instruction and after reload display the generated QR code.
  - This can then be scanned and the data should acccurately display what has been captured in the respective row.

- **Imports**
  ![image](https://github.com/user-attachments/assets/c7357ba0-7c34-4f0d-a00a-7c2db0e12096)

  -  The imports page, on load should display a File Type selection field and an upload field to upload the desired file.
  -  Two types have been accomodated for i.e CSV and XLSX. The respective selected file type should be uploaded.
  -  The format assumes the file to be as per the data directory .csv and .xlsx files respectively.
  -  After successful upload a dismissible flash message should indicate the upload was successful.
  -  Navigate to the Home page and validate the data has uploaded and displaying correctly.

**General Experience and Feedback Developing Program:**
  - The general build of the project was very challenging. The biggest part was interpreting the Delphi pascal code.
  - I installed RAD Studio to try and depict what components were used in the GUI and what field data were being captured.
  - The Capture Form depicts what I gather from it, I also saw that there were some connection which seemed like a hardware device.
  - I added the grouping of a sample view as I saw that a Sample can have mutiple readings.
  - I tried to keep the code simple and clean as much as I could.
  - It was very time consuming as I had to learn the Django framework in the last day and build the application accordingly.
  - I did pick up it was some what different to Flask but I could get up to speed quick as there were pattern elements that were the same but just done differently in Django.
  - I added Two Unit test in the app as well to demonstrate my ability to work with Unit Tests in applications, see tests.py file.
  - I picked up that were components used in the delphi program that involves a timer, spinbox and logger, I could not depict what it does so did not include it in my project
    as I thought best to leave it out then to deliver incorrect solution.
  - The status captures I also saw it was set per operation of the reading process and updated on each method execution, my project tries to simulate it by manually entering it, assuming the      individual capturing the data is the Middle/Hardware Interface processing and inputting the data.
  - The data storage I could pick up as well, in my project its demonstrated by adding the data to the database on capture.
  - The generation of QR Code is demonstrated in my project via the in line row QR generation for ease of use and better user experience. Was not sure however if the QR Code needed to be 
    downloadable or jsut scannable and I kept it at scan.
  - I trust the project I delivered meets the required needs and showcases my ability. 

