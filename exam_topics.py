# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import threading  ## Import threading

# def start_search():
#     exam_topic = combobox_exam_topic.get()
#     start_range = entry_start_range.get()
#     end_range = entry_end_range.get()

#     if not exam_topic or not start_range or not end_range:
#         messagebox.showerror("Error", "All fields must be filled out.")
#         return

#     try:
#         start_range = int(start_range)
#         end_range = int(end_range)
#     except ValueError:
#         messagebox.showerror("Error", "Start and End ranges must be numbers.")
#         return

#     # Run the search in a separate thread
#     threading.Thread(target=run_search, args=(exam_topic, start_range, end_range)).start()

# def run_search(exam_topic, start_range, end_range):
#     # Optional: Set up Chrome options
#     chrome_options = Options()
#     # Remove headless mode if you want to see the UI
#     # chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")

#     # Initialize WebDriver
#     driver = webdriver.Chrome(options=chrome_options)

#     try:
#         for i in range(start_range, end_range + 1):
#             search_query = f"{exam_topic} question {i}"
            
#             # Open Google
#             driver.get("https://www.google.com")
            
#             # Find the search box and enter the query
#             search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
#             search_box.clear()
#             search_box.send_keys(search_query)
#             search_box.send_keys(Keys.RETURN)
            
#             # Wait for the search results to load and find the first search result
#             first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
#             link = first_result.find_element(By.XPATH, '..').get_attribute('href')
            
#             # Open the first search result in a new tab
#             driver.execute_script("window.open(arguments[0]);", link)
            
#             # Go back to Google to perform the next search in the original tab
#             driver.get("https://www.google.com")

#         # Switch to the first tab to keep it as the main tab
#         driver.switch_to.window(driver.window_handles[0])

#         # Print a message and wait for 1 hour to keep the pages open
#         print("All pages opened. Keeping the pages open for 1 hour...")
#         time.sleep(3600)  # Wait for 1 hour (3600 seconds)

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     finally:
#         # Keep the browser open manually or close it if needed
#         # Uncomment the following line if you want to close the browser automatically after 1 hour
#         # driver.quit()
#         pass  # Do nothing, keep the browser open

# # List of exam topics
# exam_topics = [
#     "Exam Associate Cloud Engineer topic 1",
#     "Exam AWS Certified SysOps Administrator - Associate topic 1",
#     "Exam AWS Certified Solutions Architect - Professional SAP-C02 topic 1",
#     "Exam AWS Certified Solutions Architect - Professional topic 1",
#     "Exam AWS Certified Solutions Architect - Associate SAA-C03 topic 1",
#     "Exam AWS Certified Security - Specialty SCS-C02 topic 1",
#     "Exam AWS Certified Security - Specialty topic 1",
#     "Exam AWS Certified Machine Learning - Specialty topic 1",
#     "Exam AWS Certified DevOps Engineer - Professional DOP-C02 topic 1",
#     "Exam AWS Certified Developer - Associate DVA-C02 topic 1",
#     "Exam AWS Certified Data Engineer - Associate DEA-C01 topic 1",
#     "Exam AWS Certified Cloud Practitioner topic 1",
#     "Exam AWS Certified Advanced Networking - Specialty ANS-C01 topic 1",
#     "Exam Associate Cloud Engineer topic 1",
#     "Exam Cloud Digital Leader topic 1",
#     "Exam Professional Cloud Architect topic 1",
#     "Exam Professional Cloud Database Engineer topic 1",
#     "Exam Professional Cloud Developer topic 1",
#     "Exam Professional Cloud DevOps Engineer topic 1",
#     "Exam Professional Cloud Network Engineer topic 1",
#     "Exam Professional Cloud Security Engineer topic 1",
#     "Exam Professional Data Engineer topic 1",
#     "Exam Professional Google Workspace Administrator topic 1",
#     "Exam Professional Machine Learning Engineer topic 1",
#     "Exam 2V0-21.23 topic 1",
#     "Exam 2V0-41.23 topic 1",
#     "Exam CCSP topic 1",
#     "Exam CISSP topic 1",
#     "Exam SSCP topic 1"
# ]

# # Create the main application window
# root = tk.Tk()
# root.title("Nasser Exam Topics")  # Set the window title
# root.geometry("600x300")  # Set the initial size of the window to be larger

# # Create and place labels and entry fields with increased padding
# tk.Label(root, text="Exam Topic:").grid(row=0, column=0, padx=10, pady=10, sticky='w')

# # Create a combobox for selecting or adding exam topics
# combobox_exam_topic = ttk.Combobox(root, values=exam_topics, width=50)
# combobox_exam_topic.grid(row=0, column=1, padx=10, pady=10)
# combobox_exam_topic.set(exam_topics[0])  # Set default value

# tk.Label(root, text="Start Range:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
# entry_start_range = tk.Entry(root, width=10)
# entry_start_range.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# tk.Label(root, text="End Range:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
# entry_end_range = tk.Entry(root, width=10)
# entry_end_range.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# # Create and place the start button with increased padding
# start_button = tk.Button(root, text="Start Search", command=start_search)
# start_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# # Start the Tkinter event loop
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
import subprocess
import sys
import re

def install_webdriver_manager():
    """Install webdriver-manager if not already installed"""
    try:
        import webdriver_manager
    except ImportError:
        print("Installing webdriver-manager...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "webdriver-manager"])

def start_search():
    exam_topic = combobox_exam_topic.get()
    start_range = entry_start_range.get()
    end_range = entry_end_range.get()
    use_examtopics = var_examtopics.get()
    use_updated = var_updated.get()

    if not exam_topic or not start_range or not end_range:
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    try:
        start_range = int(start_range)
        end_range = int(end_range)
    except ValueError:
        messagebox.showerror("Error", "Start and End ranges must be numbers.")
        return

    if start_range > end_range:
        messagebox.showerror("Error", "Start range must be less than or equal to End range.")
        return

    # Update status
    status_label.config(text="Starting search...", fg="orange")
    
    # Run the search in a separate thread
    threading.Thread(target=run_search, args=(exam_topic, start_range, end_range, use_examtopics, use_updated), daemon=True).start()

def get_chrome_driver():
    """Get Chrome driver with automatic version management"""
    try:
        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        # Add user agent to avoid detection
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Error with webdriver-manager: {e}")
        try:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            
            driver = webdriver.Chrome(options=chrome_options)
            return driver
        except Exception as e2:
            print(f"Error with system ChromeDriver: {e2}")
            raise Exception("Could not initialize ChromeDriver. Please ensure Chrome and ChromeDriver are compatible.")

def get_correct_examtopics_url(exam_topic, question_number):
    """Get the correct ExamTopics URL based on the exam topic"""
    # Define URL patterns for different Cisco exams
    exam_urls = {
        "Cisco CCNA 200-301": f"https://www.examtopics.com/exams/cisco/ccna-200-301/view/{question_number}/",
        "Cisco CCNA Security": f"https://www.examtopics.com/exams/cisco/ccna-security/view/{question_number}/",
        "Cisco CCNA Wireless": f"https://www.examtopics.com/exams/cisco/ccna-wireless/view/{question_number}/",
        "Cisco CCNA CyberOps": f"https://www.examtopics.com/exams/cisco/ccna-cyberops/view/{question_number}/",
        "Cisco CCNP Enterprise": f"https://www.examtopics.com/exams/cisco/ccnp-enterprise/view/{question_number}/",
        "Cisco CCNP Security": f"https://www.examtopics.com/exams/cisco/ccnp-security/view/{question_number}/",
    }
    
    # Return the specific URL or a generic one if not found
    for key, url_template in exam_urls.items():
        if key in exam_topic:
            return url_template
    
    # Default generic URL for Cisco exams
    exam_name = exam_topic.lower().replace("cisco ", "").replace(" ", "-")
    return f"https://www.examtopics.com/exams/cisco/{exam_name}/view/{question_number}/"

def run_search(exam_topic, start_range, end_range, use_examtopics, use_updated):
    driver = None
    try:
        # Install webdriver-manager if needed
        install_webdriver_manager()
        
        # Initialize WebDriver with automatic version management
        driver = get_chrome_driver()
        status_label.config(text="Browser opened successfully", fg="green")
        
        opened_tabs = []
        failed_questions = []
        
        if use_examtopics:
            # Use ExamTopics direct access
            if use_updated:
                # Try to find the correct main page first
                if "CCNA" in exam_topic:
                    main_url = "https://www.examtopics.com/exams/cisco/ccna-200-301/"
                else:
                    main_url = "https://www.examtopics.com/exams/cisco/"
                
                driver.get(main_url)
                time.sleep(3)
                status_label.config(text=f"Opened ExamTopics main page", fg="blue")
            
            # Navigate to questions
            for i in range(start_range, end_range + 1):
                try:
                    # Get the correct URL for this question
                    question_url = get_correct_examtopics_url(exam_topic, i)
                    
                    # Try to open the question directly
                    driver.execute_script(f"window.open('{question_url}');")
                    opened_tabs.append(question_url)
                    status_label.config(text=f"Opened question {i}: {question_url}", fg="green")
                    
                    # Small delay between requests
                    time.sleep(2)
                    
                except Exception as e:
                    error_msg = f"Error opening question {i}: {str(e)[:50]}"
                    print(error_msg)
                    failed_questions.append(i)
                    status_label.config(text=f"Failed on question {i}", fg="red")
                    
                    # Try alternative URL format
                    try:
                        # Try without the exam name in URL
                        alt_url = f"https://www.examtopics.com/exams/view/{i}/"
                        driver.execute_script(f"window.open('{alt_url}');")
                        opened_tabs.append(alt_url)
                        status_label.config(text=f"Opened question {i} (alternative URL)", fg="yellow")
                        time.sleep(2)
                    except:
                        pass
        else:
            # Original Google search method
            for i in range(start_range, end_range + 1):
                try:
                    search_query = f"{exam_topic} question {i}"
                    
                    # Open Google
                    driver.get("https://www.google.com")
                    
                    # Find the search box and enter the query
                    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
                    search_box.clear()
                    search_box.send_keys(search_query)
                    search_box.send_keys(Keys.RETURN)
                    
                    # Wait for search results
                    time.sleep(2)
                    
                    # Try to find ExamTopics link first
                    try:
                        # Look for ExamTopics link in results
                        examtopics_link = driver.find_element(By.PARTIAL_LINK_TEXT, "examtopics.com")
                        link = examtopics_link.get_attribute('href')
                        if link:
                            driver.execute_script("window.open(arguments[0]);", link)
                            opened_tabs.append(link)
                            status_label.config(text=f"Opened ExamTopics for question {i}", fg="green")
                            time.sleep(1)
                            continue
                    except:
                        pass
                    
                    # If no ExamTopics link, get first result
                    try:
                        first_result = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
                        link = first_result.find_element(By.XPATH, '..').get_attribute('href')
                        
                        if link:
                            driver.execute_script("window.open(arguments[0]);", link)
                            opened_tabs.append(link)
                            status_label.config(text=f"Opened result for question {i}", fg="green")
                            time.sleep(1)
                    except Exception as e:
                        print(f"Error finding results for question {i}: {e}")
                        failed_questions.append(i)
                        status_label.config(text=f"No results for question {i}", fg="orange")
                    
                except Exception as e:
                    print(f"Error processing question {i}: {e}")
                    failed_questions.append(i)
                    status_label.config(text=f"Error on question {i}", fg="red")
                
                # Go back to Google for the next search
                driver.switch_to.window(driver.window_handles[0])
                driver.get("https://www.google.com")

        # Display summary
        summary = f"Completed! Opened {len(opened_tabs)} tabs."
        if failed_questions:
            summary += f" Failed: {len(failed_questions)} questions ({failed_questions[:5]}{'...' if len(failed_questions) > 5 else ''})"
        status_label.config(text=summary, fg="green")
        
        print(f"Opened tabs: {len(opened_tabs)}")
        if failed_questions:
            print(f"Failed questions: {failed_questions}")

    except Exception as e:
        error_msg = str(e)
        print(f"An error occurred: {error_msg}")
        status_label.config(text=f"Error: {error_msg[:60]}", fg="red")
        messagebox.showerror("Error", f"An error occurred: {error_msg}")

    finally:
        # Keep the browser open
        pass

# Updated list of exam topics with CCNA and other networking exams
exam_topics = [
    # Cisco CCNA Topics
    "Cisco CCNA 200-301",
    "Cisco CCNA Security",
    "Cisco CCNA Wireless",
    "Cisco CCNA CyberOps",
    
    # Cisco CCNP Topics
    "Cisco CCNP Enterprise",
    "Cisco CCNP Security",
    "Cisco CCNP Service Provider",
    "Cisco CCNP Collaboration",
    "Cisco CCNP Data Center",
    
    # Other Cisco Exams
    "Cisco CCIE Enterprise Infrastructure",
    "Cisco CCIE Security",
    "Cisco CCIE Service Provider",
    "Cisco CCIE Data Center",
    "Cisco CCENT",
    
    # Cloud Certifications
    "Exam Associate Cloud Engineer topic 1",
    "Exam AWS Certified SysOps Administrator - Associate topic 1",
    "Exam AWS Certified Solutions Architect - Professional SAP-C02 topic 1",
    "Exam AWS Certified Solutions Architect - Professional topic 1",
    "Exam AWS Certified Solutions Architect - Associate SAA-C03 topic 1",
    "Exam AWS Certified Security - Specialty SCS-C02 topic 1",
    "Exam AWS Certified Security - Specialty topic 1",
    "Exam AWS Certified Machine Learning - Specialty topic 1",
    "Exam AWS Certified DevOps Engineer - Professional DOP-C02 topic 1",
    "Exam AWS Certified Developer - Associate DVA-C02 topic 1",
    "Exam AWS Certified Data Engineer - Associate DEA-C01 topic 1",
    "Exam AWS Certified Cloud Practitioner topic 1",
    "Exam AWS Certified Advanced Networking - Specialty ANS-C01 topic 1",
    "Exam Associate Cloud Engineer topic 1",
    "Exam Cloud Digital Leader topic 1",
    "Exam Professional Cloud Architect topic 1",
    "Exam Professional Cloud Database Engineer topic 1",
    "Exam Professional Cloud Developer topic 1",
    "Exam Professional Cloud DevOps Engineer topic 1",
    "Exam Professional Cloud Network Engineer topic 1",
    "Exam Professional Cloud Security Engineer topic 1",
    "Exam Professional Data Engineer topic 1",
    "Exam Professional Google Workspace Administrator topic 1",
    "Exam Professional Machine Learning Engineer topic 1",
    
    # VMware Exams
    "Exam 2V0-21.23 topic 1",
    "Exam 2V0-41.23 topic 1",
    
    # Security Certifications
    "Exam CCSP topic 1",
    "Exam CISSP topic 1",
    "Exam SSCP topic 1",
    "CompTIA Security+",
    "CompTIA Network+",
    "CompTIA CySA+"
]

# Create the main application window
root = tk.Tk()
root.title("Nasser Exam Topics - CCNA Updated")
root.geometry("700x450")

# Create and place labels and entry fields with increased padding
tk.Label(root, text="Exam Topic:").grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Create a combobox for selecting or adding exam topics
combobox_exam_topic = ttk.Combobox(root, values=exam_topics, width=50)
combobox_exam_topic.grid(row=0, column=1, padx=10, pady=10)
combobox_exam_topic.set(exam_topics[0])  # Set default value to CCNA

tk.Label(root, text="Start Range:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
entry_start_range = tk.Entry(root, width=10)
entry_start_range.grid(row=1, column=1, padx=10, pady=10, sticky='w')
entry_start_range.insert(0, "1")  # Default value

tk.Label(root, text="End Range:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
entry_end_range = tk.Entry(root, width=10)
entry_end_range.grid(row=2, column=1, padx=10, pady=10, sticky='w')
entry_end_range.insert(0, "10")  # Default value

# Add checkbox for ExamTopics direct access
var_examtopics = tk.BooleanVar()
var_examtopics.set(True)  # Default to ExamTopics for CCNA
checkbox_examtopics = tk.Checkbutton(root, text="Use ExamTopics Direct Access (CCNA)", 
                                     variable=var_examtopics)
checkbox_examtopics.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Add checkbox for updated URL format
var_updated = tk.BooleanVar()
var_updated.set(True)  # Default to updated URLs
checkbox_updated = tk.Checkbutton(root, text="Use Updated ExamTopics URL Format", 
                                  variable=var_updated)
checkbox_updated.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Create and place the start button
start_button = tk.Button(root, text="Start Search", command=start_search, 
                        bg="lightblue", fg="black", font=("Arial", 10, "bold"))
start_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Add a status label at the bottom
status_label = tk.Label(root, text="Ready to search CCNA exam questions", fg="green", wraplength=600)
status_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Update status when combobox changes
def on_topic_change(event):
    selected = combobox_exam_topic.get()
    if "CCNA" in selected or "Cisco" in selected:
        var_examtopics.set(True)
        status_label.config(text=f"Searching {selected} on ExamTopics", fg="green")
    else:
        var_examtopics.set(False)
        status_label.config(text=f"Searching {selected} on Google", fg="blue")

combobox_exam_topic.bind('<<ComboboxSelected>>', on_topic_change)

# Add some helpful text
help_label = tk.Label(root, text="Tip: For CCNA questions, use ExamTopics with the updated URL format", 
                     fg="gray", font=("Arial", 8))
help_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()

