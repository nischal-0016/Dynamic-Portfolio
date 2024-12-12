# portfolio-app
Installation and Setup

1. Clone the Repository
```bash
git clone https://github.com/your-username/dynamic-portfolio.git
cd dynamic-portfolio
```

2. Set up a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate. On mac, use `source env/bin/activate

```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Apply Migrations
```bash
py manage.py makemigrations
py manage.py migrate
```

5. Create a Superuser 
``` bash
py manage.py createsuperuser
```

6. Run the Development Server
```bash
py manage.py runserver
```

7. Access the Site 
```bash
Open your browser and navigate to http://127.0.0.1:8000/.
```

The portfolio website is designed to dynamically fetch data from the database, making it easy to update content without touching the code. Here’s how a non-coder can manage the data:

Step 1: Access the Admin Panel
Open your browser and navigate to the Admin Panel by visiting: http://127.0.0.1:8000/admin/

Log in using the admin credentials. If you don’t have these, ask the developer or admin of the project for access.

Step 2: Managing Your Data
Once logged in, you’ll see a dashboard with all the available models. Here’s how to manage each section:

Profile Section
* Click on Profiles.
* To add a new profile, click Add Profile and fill in the details:
    * Name: Your name.
    * Title: Your professional title (e.g.,         "Software Developer").
    * Image: Upload your profile picture.
* Save your changes.

About Me Section
* Click on About Details or About Me.
* To update your introduction, edit the existing About Me record.
* To add or modify details, go to About Details, and add/edit records:
    * Title: A short heading (e.g., "Who I Am").
    * Description: A detailed explanation of that section.
    * Optionally, upl-oad an Arrow Image for visual enhancement.

Skills Section
* Click on Skills.
Add or update your skills:
Name: The skill name (e.g., "Python").
Category: Choose between Frontend or Backend.
Level: Enter the skill level (e.g., "Expert", "Intermediate").

Projects Section
* Click on Projects.
* Add or edit a project:
    * Title: The project’s name.
    * Description: A brief overview of the project.
    * Image: Upload an image showcasing the project.
    * Live Demo URL: Provide a link to the live demo of your project.

Contact Section
* Click on Contact.
* Add your contact details:
    * Email: Your email address.
    * Message: Write a default message if needed.
    * Facebook URL: Add your Facebook profile link.
    * Twitter URL: Add your Twitter profile link.
    * Phone Nuber: Add your Contact Number.

Step 3: Save and Preview Changes
* After making updates, click the Save button at the bottom of the form.
* Visit your portfolio site (e.g., http://127.0.0.1:8000/) to see the updated content.

