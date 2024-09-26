# Personal Website

This repository contains the code for my personal website, which highlights my AI consultancy services, projects, and professional background. The website is built with **Streamlit** and offers a clean and professional user interface.

## 🖥️ Live Demo

You can view the live version of the website [here](#).

## 🚀 Features

- **Interactive Navigation**: Sidebar navigation for easy access to different sections.
- **Custom Styling**: Tailored design with CSS for a modern, professional look.
- **Home Section**: Overview of my AI consultancy services and expertise.
- **About Me Section**: Detailed background about my AI journey, education, and professional experiences.
- **Services Section**: Information about the AI services I offer, including strategy development, machine learning, NLP, and workshops.
- **Portfolio Section**: Showcase of client projects and research contributions.
- **Testimonials Section**: Feedback from clients and colleagues.
- **Contact Form**: Integrated form for visitors to reach out to me via email.

## 📄 Code Structure

Here's an overview of the main sections in the code:

- **Streamlit Setup**: Configures the app layout, page title, and icons.
- **Custom CSS**: Injected for styling elements like fonts, colors, and section titles.
- **Sidebar Navigation**: Allows users to navigate between sections like Home, About Me, Services, Portfolio, Testimonials, and Contact.
- **Image Handling**: Uses `PIL.Image` for image loading and display.
- **Form Integration**: A custom contact form embedded using HTML and integrated with FormSubmit for message handling.

## 🛠️ Built With

- **Framework**: [Streamlit](https://streamlit.io/)
- **Image Handling**: [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- **Form Handling**: [FormSubmit](https://formsubmit.co/)
- **Styling**: Custom CSS through Streamlit's `markdown` feature.

## 📦 Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://docs.streamlit.io/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/personal-website.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd personal-website
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

   The app will be accessible at `http://localhost:8501/`.

### Adding Your Own Image

Replace the placeholder image in the **Home Section** with your own:

```python
image = Image.open('your_image_path.jpg')  # Replace with your image path
```

### Deployment

You can deploy the app using [Streamlit Cloud](https://streamlit.io/cloud), [Heroku](https://www.heroku.com/), or any preferred hosting platform.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Contributing

Feel free to contribute to this project by submitting a pull request or opening an issue.

## 📧 Contact

If you'd like to reach out, you can contact me via [LinkedIn](https://www.linkedin.com/in/ak901d/) or email me at [abdullahkhanai@icloud.com](mailto:abdullahkhanai@icloud.com).
