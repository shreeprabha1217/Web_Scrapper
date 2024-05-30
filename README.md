DOCUMENTATION OVER MY APPORACH TO BUILD SCRAPPER TO SCRAPE GRAB FOOD DELIVERY. 

 

    QUALITY CONTROL METHODS 

	I have extracted data of the restaurants present over each locations specified. Each of this file contains the data about the restaurants present in respective locations. I have taken card name given for restaurants and using the loop obtained all the restaurants present in the card. 

Tools used for extracting data: 

    BeautifulSoup – BeautifulSoup was used to extract data from the HTML source code of the Grab Food Delivery website. It allowed the scraper to locate specific elements, such as restaurant names and cuisine information, within the webpage's HTML structure. 

                      2.    Selenium - Selenium was used in conjunction with a web browser (Chrome) 	               to simulate user interactions, such as entering search queries and clicking 	               buttons, on the Grab Food Delivery website. 

                      3.   ChromeDriver- ChromeDriver was used as the WebDriver backend for 		               Selenium to control and automate the Chrome browser during the scraping 	               process. 

 

    APPROACH AND METHADOLOGY 

	I am not someone who is thorough with Python, but when I first read the assignment     and saw 'web scraping,' I remembered that there was a topic on this in our engineering syllabus where they had explained about BeautifulSoup and Selenium. That's when I decided to complete this assignment using Python. 

Later, I went through a GeeksForGeeks tutorial on 'Python Web Scraping Tutorial' and referred to some of the ChatGPT code. 

It was not that difficult for me to grasp since I worked as a test engineer before, and back then, I had used Selenium with Java myself to learn more about automation. Using that knowledge, I could easily identify the divisions' names from the HTML code and use them in the Python code to extract data about the restaurants. 

Later, I went through each block of code I found online and worked on understanding what each block of code does. That's how I could complete the assignment in Python, even though I am not very familiar with the language. 

    CHALLENGES FACED DURING SCRAPING PROCESS 

	I have faced certain issues while solving this assignment, I was repeatedly getting an error  

“ ERROR - Error during scraping location 'PT Singapore - Choa Chu Kang North 6, Singapore, 689577': Message:  

Stacktrace: 

#0 0x557ccdd95dc3 <unknown> 

#1 0x557ccda844e7 <unknown> 

#2 0x557ccdacf35d <unknown> 

#3 0x557ccdacf411 <unknown> 

#4 0x557ccdb12774 <unknown> 

#5 0x557ccdaf147d <unknown> 

#6 0x557ccdb0fc29 <unknown> 

#7 0x557ccdaf11f3 <unknown> 

#8 0x557ccdac228a <unknown> 

#9 0x557ccdac2c5e <unknown> 

#10 0x557ccdd5a0eb <unknown> 

#11 0x557ccdd5e03b <unknown> 

#12 0x557ccdd46201 <unknown> 

#13 0x557ccdd5eba2 <unknown> 

#14 0x557ccdd2b0bf <unknown> 

#15 0x557ccdd84f18 <unknown> 

#16 0x557ccdd850f0 <unknown> 

#17 0x557ccdd94f14 <unknown> 

#18 0x7f27e2f09609 start_thread” 

 

Approach- I referred so many sites, documentation, chatgpt to solve this error but none could provide answer for What actually is causing this. Later I removed the option in my code “ options.add_argument(‘--headless’) “ just with the hope of seeing what is happening on the browser. But for my wonder it worked fine then immediately when I tried running the program I got an error saying server is busy or couldn’t connect to the server. Later I realized it’s just the server causing error sometimes.  Upon solving this I got few more errors but it was all because of one particular wrong division name given by me. Apart from this it was all learning process for me to understand each unit of code.  

 

 

    IMPROVEMENTS OR OPTIMIZATIONS 

 

	Optimize waiting time : Instead of using fixed sleep times (e.g., time.sleep(2) and time.sleep(10)), use dynamic waiting strategies such as WebDriverWait with expected_conditions to wait for specific elements to appear before proceeding. 

 

	Error handling : Enhance error handling mechanisms to gracefully handle exceptions that may occur during scraping. This includes handling cases where expected elements are not found or encountering unexpected errors. 

 

    STEPS TO EXECUTE LOCALLY 

 

Install Python : 

	sudo apt update 

sudo apt install python3 

Install BeautifulSoup, Selenium, WebDriver : 

	sudo apt install python3-pip 

	pip install beautifulsoup4 

	pip install selenium 

	pip install webdriver-manager 

Run the Program: 

	python3 grab_food.py 

	python3 read_gzip_file.py  --> To read the contents stored in the output file 

 

	 

 

 

                     

 

 

 
