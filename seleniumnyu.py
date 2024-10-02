from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gtts import gTTS
import playsound
import os
import base64

import sounddevice as sd
import soundfile as sf


def speak(file):
    # Read the audio file
    data, samplerate = sf.read(file)
    
    # Play the audio file
    sd.play(data, samplerate)
    
    # Wait until the audio file is finished playing
    sd.wait()

class cv_test:
    def __init__(self):
        from selenium import webdriver
        # Initialize the WebDriver (e.g., for Chrome)
        driver = webdriver.Chrome()
        speak('Opening_Northeastern_University_website.mp3')
        driver.get("https://www.northeastern.edu/")
        time.sleep(5)
        # Open the webpage
        speak('Navigating_to_the_login_page.mp3')
        driver.get('https://enroll.northeastern.edu/apply/')
        # Replace with the actual login URL
        
        link = driver.find_element(By.XPATH, "//a[contains(text(), 'Log in')]")
        link.click()
        time.sleep(5)
        speak('Entering_login_details.mp3')
        # Find the email input field and enter the email
        email_field = driver.find_element(By.ID, 'email')  # Replace 'email' with the actual ID if different
        email_field.clear()
        email_field.send_keys('janeshvar2004@gmail.com')

        # Find the password input field and enter the password
        password_field = driver.find_element(By.ID, 'password')  # Replace 'password' with the actual ID if different
        password_field.clear()
        password_field.send_keys('Konectu@12345')
        time.sleep(1)

        # Find the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        login_button.click()
        time.sleep(5)
        # Find the button by its onclick attribute and click it
        speak('selecting_the_required_application.mp3')
        link = driver.find_element(By.XPATH, "//a[contains(text(), 'Northeastern University Application (2025-2026)')]")
        link.click()

        time.sleep(3)
        speak('opening_application.mp3')
        button = driver.find_element(By.XPATH, '//button[contains(@onclick, "FW.Lazy.Commit")]')
        button.click()
        time.sleep(5)
        speak('Entering_Biographical_information.mp3')
        title_select = Select(driver.find_element(By.ID, 'form_35561e0c-ed90-433b-a7ba-0105a362347b'))
        title_select.select_by_value('Mr.')
        time.sleep(1)
        # Fill the text input for first name
        first_name_input = driver.find_element(By.ID, 'form_e8b26afc-a0f5-4244-bdcd-9d36b8a3cc13')
        first_name_input.clear()
        first_name_input.send_keys('Sundar')
        time.sleep(1)
        # Fill the text input for middle name
        middle_name_input = driver.find_element(By.ID, 'form_b8f966ab-3204-46fc-819e-f33006a6c6c1')
        middle_name_input.clear()
        middle_name_input.send_keys('Kumar')
        time.sleep(1)
        # Fill the text input for last name
        last_name_input = driver.find_element(By.ID, 'form_461c87e0-7bba-42ec-aff9-145486337132')
        last_name_input.clear()
        last_name_input.send_keys('Kennedy')
        time.sleep(1)
        # Select Jr. from the dropdown
        suffix_select = Select(driver.find_element(By.ID, 'form_49eda08c-518d-4622-bd1e-a2dccd943bcb'))
        suffix_select.select_by_value('Jr.')
        time.sleep(1)

        input = driver.find_element(By.ID, 'form_bf2e5743-489c-4814-9b64-a43ed27bd636')
        input.clear()
        input.send_keys('Kennedy')
        time.sleep(1)
        add_address_link = driver.find_element(By.CSS_SELECTOR, 'a.widget_add')
        add_address_link.click()

        # Wait for the popup to appear and interact with it
        wait = WebDriverWait(driver, 10)

        # Select "United States" from the country dropdown
        country_select = wait.until(
            EC.visibility_of_element_located((By.ID, 'form_8cdf7a90-03b9-47af-9c8e-6e01f61553fd_country')))
        country_dropdown = Select(country_select)
        # country_dropdown.select_by_value('United States')

        # Enter address into the textarea
        address_textarea = driver.find_element(By.ID, 'form_8cdf7a90-03b9-47af-9c8e-6e01f61553fd_street')
        address_textarea.clear()
        address_textarea.send_keys('1234 Elm St, El Cerrito, NY 10001 ')

        # Fill the Previously Used Last Name field
        state_select = driver.find_element(By.ID, 'form_8cdf7a90-03b9-47af-9c8e-6e01f61553fd_region')
        state_dropdown = Select(state_select)
        state_dropdown.select_by_visible_text('New York')
        time.sleep(1)
        postal_code_input = driver.find_element(By.ID, 'form_8cdf7a90-03b9-47af-9c8e-6e01f61553fd_postal')
        postal_code_input.clear()
        postal_code_input.send_keys('10001')
        time.sleep(1)
        address_type_select = driver.find_element(By.ID, 'form_0e96fec5-c52f-40f4-a8d4-a26e376734bc')
        address_type_dropdown = Select(address_type_select)
        address_type_dropdown.select_by_value('mailing')
        time.sleep(1)
        # Click the "Save" button
        save_button = driver.find_element(By.CSS_SELECTOR, 'button.default[onclick*="Form.Validate(this)"]')
        save_button.click()

        # Optionally, wait for and click the "Skip Validation" button if it appears
        # skip_validation_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Skip Validation"]')))
        # skip_validation_button.click()
        time.sleep(2)
        phone_input = driver.find_element(By.ID, 'form_bd31dc60-d1e4-4cad-95cc-e4318c94642f')
        phone_input.clear()
        phone_input.send_keys('+91 11111111111')
        time.sleep(1)
        from selenium import webdriver
        '''

        # Assuming driver is already initialized and points to the page with the select element
        select_element = driver.find_element_by_id('form_e50fd210-d6cf-4081-a294-7f0b5755e877')
        select = Select(select_element)
        select.select_by_value('0')'''

        # select = Select(WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.ID, 'form_e50fd210-d6cf-4081-a294-7f0b5755e877'))))
        # select.select_by_visible_text('No')
        # Set gender to Male
        gender_select = driver.find_element(By.ID, 'form_602f1f96-20f8-4e3a-bc53-92759e309eb1')
        gender_dropdown = Select(gender_select)
        gender_dropdown.select_by_value('M')
        time.sleep(1)
        gender_id = driver.find_element(By.ID, 'form_f762753c-786a-4281-b5c0-8eb9ce32bfbf')
        gender_id.send_keys('Straight')
        time.sleep(1)
        gender_id = driver.find_element(By.ID, 'form_af7a3fcb-245d-4925-bf9d-0ab3aecdf4ba')
        gender_id.send_keys('he')
        time.sleep(1)
        # Set country to USA
        # Click on the select2 dropdown to open options
        country_dropdown = driver.find_element(By.CSS_SELECTOR, 'span.select2-selection--single')
        country_dropdown.click()

        time.sleep(1)
        # Wait for the dropdown options to load and select USA
        country_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//ul[@id="select2-form_54e8094e-4db3-4d05-83f4-ebc1064ce336-results"]//li[text()="United States"]'))
        )
        country_option.click()

        # Click "Continue" button

        # Wait until the dropdown is clickable
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection--single"))
        )

        # Click the dropdown to open it
        dropdown.click()

        # Wait for the dropdown options to be visible and select an option
        option_to_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'United States')]"))
        )
        time.sleep(1)
        # Click the desired option
        option_to_select.click()
        time.sleep(1)
        speak('moving_to_the_next_page.mp3')
        continue_button = driver.find_element(By.CSS_SELECTOR, 'button.default[onclick*="FW.Validate(this)"]')
        continue_button.click()
        time.sleep(1)

        # Wait for a few seconds to observe the result
        time.sleep(5)
        speak('entering_program_information.mp3')
        select1 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_d2906b6e-4cbc-45d9-99d8-8e63fbe4655c'))
        ))
        select1.select_by_visible_text('Graduate Program Application')
        time.sleep(1)
        # Select "College of Engineering"
        select2 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_8ffab95c-93a5-4549-a48d-b7b593449ebd'))
        ))
        select2.select_by_visible_text('Khoury College of Computer Sciences')
        time.sleep(2)
        # Select "Khoury College of Computer Sciences"
        select3 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_110e4761-1eb6-44b2-8fa7-fb9b7cba60c4'))
        ))
        select3.select_by_visible_text('Computer Science')
        time.sleep(1)
        # Select "Master of Science"
        select4 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_126af68c-87cb-473a-b711-a2219350ce87'))
        ))
        select4.select_by_visible_text('Master of Science')
        time.sleep(1)

        # Select "Full-time"
        select5 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_cd7ebc9f-3df7-40ee-9bf9-57e716f3615b'))
        ))
        select5.select_by_visible_text('Full-time')
        time.sleep(1)
        # Select "Spring 2025"
        select6 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_30e0fd6d-47d8-4e8f-a71a-028629d68a71'))
        ))
        select6.select_by_visible_text('Spring 2025')
        time.sleep(1)
        # Select "On Ground"
        select7 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_4055c88f-b8dc-41ac-9775-85905fb4d743'))))
        select7.select_by_visible_text('On Ground')

        # Click "No"
        time.sleep(1)

        select8 = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'form_ef68aeb7-6d5d-4b23-9232-9cb7262b6658'))))
        select8.select_by_visible_text('Boston, MA')

        no_label = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="form_d0f0392c-f1d6-458f-bc3e-b932b0336587_2"]'))
        )
        no_label.click()
        speak('moving_to_the_next_page.mp3')
        time.sleep(1)
        # Click the "Continue" button
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(4)
        speak('Answering_Campus_Specific_Questions.mp3')

        radio_button_no = driver.find_element(By.ID, "form_9b553d8b-6bb4-4cfd-8757-90849a265ab7_2")
        radio_button_no.click()
        time.sleep(1)
        # Fill in the checkbox (American Indian or Alaska Native)
        checkbox_native = driver.find_element(By.ID, "form_3c10b2a0-047f-4cf9-9131-6a04f0b20e3c_1")
        checkbox_native.click()
        time.sleep(1)
        # Select 'Yes' for the third radio button
        radio_button_yes = driver.find_element(By.ID, "form_2347fde8-80fb-4312-8cb5-2dc924979835_1")
        radio_button_yes.click()
        time.sleep(1)
        # Select 'No' for the fourth radio button
        radio_button_no_2 = driver.find_element(By.ID, "form_85f0956b-d48e-4d26-9c7f-0b35df660462_2")
        radio_button_no_2.click()
        # Click the "Continue" button
        speak('moving_to_the_next_page.mp3')
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        time.sleep(1)
        continue_button.click()
        time.sleep(6)
        speak('entering_application_information.mp3')
        form_ids = [
            'form_19eb6655-1760-46d5-944e-bd34824e3ef9_2',
            'form_d5a438e7-8b42-4b54-b19b-99676ed00138_2',
            'form_9ca6ba4c-046a-45e4-8310-ebde5e13d256_2',
            'form_6520ae77-c2f8-4dca-a523-6a9faed1070a_2',
            'form_6da0b7b1-515d-4e97-8ba9-a43a3f7cea81_2',
            'form_b7452032-e863-4397-a839-c4d7b37dc8d1_2',
            'form_a29e4528-ff6c-4f65-950c-fdec51b9ac5e_2',
            'form_f0011ffd-56f3-4f9e-86b5-20370a9a4249_2'
        ]

        # Iterate through each form ID and select the "No" option
        for form_id in form_ids:
            no_option = driver.find_element(By.ID, form_id)
            if not no_option.is_selected():
                no_option.click()
            time.sleep(1)
        speak('moving_to_the_next_page.mp3')
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )

        continue_button.click()
        # Close the WebDriver
        time.sleep(5)
        speak('Answering_Legal_Questions.mp3')
        radio_button_no = driver.find_element(By.ID, "form_68cc9701-c6ad-432e-96fd-9b87173495af_2")
        radio_button_no.click()
        time.sleep(1)
        # Fill in the checkbox (American Indian or Alaska Native)
        checkbox_native = driver.find_element(By.ID, "form_c90f2463-5fcf-4ac2-b77f-22db380041b3_2")
        checkbox_native.click()
        time.sleep(1)
        # Select 'Yes' for the third radio button
        radio_button_yes = driver.find_element(By.ID, "form_3b7890c2-7509-4d83-bfe8-8d11984c101d_2")
        radio_button_yes.click()
        speak('moving_to_the_next_page.mp3')
        time.sleep(1)
        # Select 'No' for the fourth radio butto

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default')))
        continue_button.click()

        time.sleep(4)
        speak('Entering_academic_information.mp3')
        activities_textarea = driver.find_element(By.ID, "form_c5727cb6-2af7-40f4-9f6c-ef51144735a2")
        time.sleep(1)
        # Input fake information for activities
        activities_text = "President of Computer Science Club; Organizer of AI Conference 2023; Volunteer at Local Animal Shelter; Member of College Debate Team; Developer at Open Source Project;"
        activities_textarea.send_keys(activities_text)
        time.sleep(1)
        # Locate the second textarea (Honors, Fellowships, or Non-Academic Distinctions)
        honors_textarea = driver.find_element(By.ID, "form_77f95777-0d67-457f-a878-008012f12784")
        time.sleep(1)
        # Input fake information for honors and distinctions
        honors_text = "Dean's List for Academic Excellence; Best Paper Award at ML Symposium 2023; Research Fellow at National Science Foundation; Published Article in AI Journal;"
        honors_textarea.send_keys(honors_text)

        time.sleep(1)
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(4)
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(5)

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(5)

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(5)

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(5)
        speak('Entering_supplementary_information.mp3')
        textarea = driver.find_element(By.ID, 'form_7b26f286-ec0b-407d-9f88-762551fd996e')

        # Step 2: Fill the textarea with the given text
        time.sleep(1)
        text_to_fill = """
        Desktop PCs

        Windows: Excellent
        Linux: Good
        macOS: Fair
        Laptops

        Windows: Excellent
        Linux: Good
        macOS: Fair
        Servers

        Windows Server: Good
        Linux Server (e.g., Ubuntu, CentOS): Good
        macOS Server: Fair
        Workstations

        Windows Workstations: Excellent
        Linux Workstations: Good
        macOS Workstations: Fair
        Operating Systems
        Windows 10/11: Excellent
        Ubuntu: Good
        CentOS/RHEL: Good
        macOS (latest versions): Fair
        Windows Server 2019/2022: Good
        Debian: Good
        Fedora: Fair
        Arch Linux: Fair
            """
        time.sleep(1)
        textarea.send_keys(text_to_fill)
        # Step 1: Fill the first textarea with fake information
        textarea1 = driver.find_element(By.ID, 'form_2f908266-0523-449d-977c-ce9e35e88c66')
        time.sleep(1)
        text1 = """
            Introduction to Computer Science, XYZ University, 01/2020, "Introduction to CS", A
            Data Structures, ABC College, 05/2021, "Data Structures and Algorithms", B+
            Algorithms, DEF Institute, 09/2022, "Algorithms Unlocked", A-
            Operating Systems, GHI University, 01/2023, "Operating Systems: Three Easy Pieces", B
            """
        textarea1.send_keys(text1)
        time.sleep(1)
        # Step 2: Fill the second textarea with fake information
        textarea2 = driver.find_element(By.ID, 'form_0c075052-03ab-4b54-967b-9c4492d224e0')
        text2 = """
            Python; 2000
            Java; 1500
            C++; 1800
            JavaScript; 1200
            """
        textarea2.send_keys(text2)

        time.sleep(5)
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()
        time.sleep(5)
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(5)
        speak('entering_signature.mp3')
        input_field = driver.find_element(By.CSS_SELECTOR, 'input[name="signature"]')

        # Enter the name into the input field
        input_field.send_keys('Sundar Kumar Kennedy')
        speak('moving_to_the_next_page.mp3')
        time.sleep(2)
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()


        time.sleep(5)
        speak('submitting_form.mp3')
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.default'))
        )
        continue_button.click()

        time.sleep(5)
        # Close the browser after logging in
        driver.quit()