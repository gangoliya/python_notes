# Python Automation Modules

## Module 0: The  Foundation
- Virtual environments
- Activating & deactivating the virtual environments
- PIP
- Installing packages through PIP
- pip freeze > requirements.txt
- pip install -r requirements.txt
- Structuring of a project
- Benefits of clean project
- uv package manager
<br>

## Module 1: File System Automation
- __Key librarires__: `pathlib`, `os` & `shutil`
- Get the current working directory: `pathlib.Path.cwd()`
- Create new folder: `.mkdir()`
- Listing all files & directories: `.iterdir()`
- Create `.touch()`, rename `.rename()`, move `.replace()`, and delete `.unlink()` `.rmdir()` files & folders
- Recursively walk through directory trees to find specific files `.rglob()`
- Verify if a path exists `.exists()`, if it's a file `.is_file()`, or if it's a directory `.is_dir()`
- Read from `.read_text()` and write to `.write_text()` text files
- __Mini-Project Idea:__ Create a script that organizes the user's "Downloads" folder. It should read all files and move them into subfolders based on their file type (e.g., .jpg, .png go to an "Images" folder; .pdf go to a "Documents" folder, etc.)
<br>

## Module 2: Working with Common Data Formats
- __Key librarires__: `CSV`, `openpyxl`, `JSON`, `PyPDF2` & `pypdf`
- __CSV__ module
- __Excel Spreadsheets:__ Introduce the __openpyxl__ library. Cover reading from specific cells, iterating over rows/columns, creating new sheets, and writing data back to an .xlsx file.
- __JSON Data:__ Use the built-in __json__ module. Explain the JSON format (key-value pairs) and its direct mapping to Python dictionaries. Cover json.load() (to read from a file) and json.dump() (to write to a file).
- __PDFs:__ Introduce __PyPDF2__ or __pypdf__. Show how to extract text from PDFs, merge multiple PDFs into one document, and split a single PDF into several smaller ones.
- __Mini-Project Idea:__ Read employee data from a provided CSV file. For each employee, generate a simple "Welcome Letter" as a text file. As a bonus, read sales data from an Excel sheet and generate a summary report
<br>

## Module 3: Web Automation and Scrapping

### Part 1: Web Scrapping - Getting Data from Websites
- __Key librarires__: `requests` & `Beautiful Soup 4`
- Basics of HTML(tags, classes, IDs)
- __GET request__
- Show how to parse the response content with BeautifulSoup to __find specific HTML elements__ and extract their text or attributes
- __Ethics:__ Stress the importance of __ethical scraping__: always check a website's robots.txt file, avoid overwhelming a server with too many requests (introduce time.sleep()), and identify your script with a User-Agent header
<br>

### Part 2: Browser Automation (Controlling a Web Browser)
- __Key librarires__: `Selenium`
- Explain when to use Selenium (e.g., for websites that rely heavily on JavaScript, for automating logins, filling out forms, or clicking buttons)
- How to __set up WebDriver__ (e.g., for Chrome or Firefox)
- __Actions:__ Show how to open a URL, __find elements__ using various locators (ID, class name, XPath, CSS selector), __type text__ into input fields, __click buttons__, and __wait for elements__ to appear on a dynamically loaded page.
- __Mini-Project Idea:__ Write a script that scrapes the titles and prices of the top 5 products for a specific search term on an e-commerce website. As a follow-up, use Selenium to automate logging into a social media site (using a dummy account on a test site, if available)
<br>

## Module 4: Interacting with APIs
- __Key librarires__: `requests`
- __What is an API?__ Explain it as a structured way for different software programs to communicate with each other.
- __Anatomy of an API request:__ Endpoint (the URL), HTTP Methods (GET for retrieving data, POST for sending data), and Headers (often used for authentication or specifying data types).
- __Authentication:__ Explain the concept of __API keys__ and how they grant access.
- __Working with JSON responses:__ Show how the JSON data returned by APIs can be easily parsed into Python dictionaries and lists.
- __Mini-Project Idea:__ Use a free, public API, such as the [OpenWeatherMap API](https://openweathermap.org/api) or a public joke API. The student's script should take user input (e.g., a city name) and print out relevant information obtained from the API (e.g., current weather conditions for that city)
<br>

## Module 5: Task Scheduling and System Automation
- __Key librarires__: `Task Scheduler` & `cron`
- __Schedule library:__ A simple, human-readable way to __schedule tasks within a Python script__ itself (e.g., schedule.every().day.at("10:30").do(my_job)). This is great for simple, in-script scheduling.
- __OS-level Schedulers:__ Explain how to leverage the operating system's native tools for more robust and system-wide scheduling of Python scripts.
    - __Windows:__ `Task Scheduler`
    - __Linux/macOS:__ `cron`
- __Subprocess module:__ Teach how to use this built-in module to __run other command-line tools or scripts__ directly from within a Python script
- __Mini-Project Idea:__ Take the "Downloads Folder Organizer" script from Module 1 and use schedule to make it run automatically every day at a specific time (e.g., 6 PM). Then, for advanced students, guide them on how to set it up using their operating system's scheduler
<br>

## Module 6: GUI Automation
- __Key librarires__: `PyAutoGUI`
- __Mouse Control:__ Moving the mouse, clicking, and dragging
- __Keyboard Control:__ Typing strings, pressing individual keys, and using hotkeys (e.g., Ctrl+C, Alt+Tab)
- __Image Recognition:__ Taking screenshots and using basic image recognition to find where an image of a button or icon is on the screen to click it
- __Warning:__ Emphasize that these scripts are __inherently brittle__. They can break easily if the screen resolution changes, the application layout is modified, or icons are updated, as they rely on visual positioning
- __Mini-Project Idea:__ Automate a simple, repetitive task within a basic desktop application like Calculator or Notepad. For instance, open Notepad, type a predefined message, and then save the file to a specific location using only PyAutoGUI
<br>

## Module 7: Other Tools
- Apache Flink, etc.
- Mini project based on Finance APIs to track stocks for their opening & closing volume, PE ratios & Volumes