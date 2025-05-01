# BlogX - A Modern Django Blog Application

BlogX is a feature-rich blog application built with Django, featuring a clean and modern UI with Tailwind CSS.

## Features

- 🎨 Modern UI with Tailwind CSS
- 📝 Rich text editor for blog posts
- 🖼️ Image upload support with thumbnails
- 📱 Responsive design
- 📄 Pagination for blog posts
- 🔍 Clean and intuitive navigation

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, Tailwind CSS
- **Database**: SQLite
- **Rich Text Editor**: CKEditor
- **Image Handling**: Django's built-in image handling

## Project Structure

```
blogger/
├── blog/                    # Main blog application
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── home.html       # Home page with blog list
│   │   ├── detail.html     # Blog post detail page
│   │   └── create.html     # Create new blog post page
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL routing
│   └── forms.py            # Form definitions
├── blogger/                 # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── media/                   # User uploaded files
└── manage.py               # Django management script
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blogger
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Creating a Blog Post
1. Navigate to the home page
2. Click the "+ Create Post" button
3. Fill in the title and content
4. Optionally upload a thumbnail image
5. Click "Post" to publish

### Viewing Posts
- Home page shows a paginated list of all posts
- Click on any post to view its full content
- Use pagination controls to navigate through posts

## Features in Detail

### Blog Post Model
- Title: CharField (max_length=200)
- Body: RichTextField (using CKEditor)
- Thumbnail: ImageField (optional, with default image)
- Created/Updated timestamps

### UI Features
- Responsive design that works on all devices
- Clean and modern interface using Tailwind CSS
- Image thumbnails for blog posts
- Rich text editing capabilities
- Pagination for better content organization


## Acknowledgments

- Django for the amazing web framework
- Tailwind CSS for the utility-first CSS framework
- CKEditor for the rich text editing capabilities
