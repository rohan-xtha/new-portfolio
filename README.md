<div align="center">

# 🚀 Rohan Shrestha — Portfolio

**A modern, animated developer portfolio built with pure HTML, CSS & JavaScript**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Web3Forms](https://img.shields.io/badge/Web3Forms-0090FF?style=for-the-badge&logo=maildotru&logoColor=white)](https://web3forms.com)

[**Live Demo →**](#) · [**Report Bug →**](https://github.com/your-username/portfolio/issues) · [**Request Feature →**](https://github.com/your-username/portfolio/issues)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Dark Glassmorphism** | Premium dark theme with glass-morphic cards and frosted blur effects |
| ⚡ **Animated Typing** | Dynamic typewriter effect cycling through developer roles |
| 🌌 **Floating Particles** | Randomized cyan & purple particle animation in the hero section |
| 📊 **Skill Bars** | Animated progress bars that fill on scroll using Intersection Observer |
| 🔢 **Stat Counters** | Smooth number counter animations triggered on viewport entry |
| 📱 **Fully Responsive** | Mobile-first design that looks great on all devices |
| 📬 **Working Contact Form** | Real email delivery via [Web3Forms](https://web3forms.com) — no backend needed |
| 🎭 **Scroll Reveal** | Staggered fade-in animations as sections enter the viewport |
| 🍔 **Mobile Menu** | Animated hamburger menu with smooth open/close transitions |
| ⚙️ **Zero Dependencies** | No frameworks, no build tools — just vanilla HTML, CSS & JS |

---

## 📸 Preview

<div align="center">

| Desktop | Mobile |
|---------|--------|
| ![Desktop Preview](#) | ![Mobile Preview](#) |

</div>

> 💡 *Replace the preview links above with actual screenshots of your deployed site.*

---

## 🏗️ Project Structure

```
portfolio/
├── index.html      # Main HTML — all sections (Hero, About, Skills, Projects, Experience, Contact)
├── style.css       # Complete styling — design tokens, responsive breakpoints, animations
├── script.js       # Interactivity — typing effect, scroll reveal, particles, form submission
└── README.md       # You are here!
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/portfolio.git
cd portfolio
```

### 2. Open in browser

Simply open `index.html` in your browser — no build step or server required!

```bash
# Or use a local dev server (optional)
npx serve .
```

### 3. Configure the contact form

The contact form uses **Web3Forms** for email delivery. To set up your own:

1. Go to [web3forms.com](https://web3forms.com) and enter your email to get an access key
2. Open `index.html` and find this line:
   ```html
   <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
   ```
3. Replace `YOUR_ACCESS_KEY_HERE` with your actual key
4. That's it! Form submissions will arrive in your inbox 📬

---

## 🎨 Customization

### Colors & Design Tokens

All design tokens live in the `:root` block at the top of `style.css`:

```css
:root {
    --bg-primary: #0a0a0f;           /* Page background */
    --accent-cyan: #00d4ff;          /* Primary accent */
    --accent-purple: #8b5cf6;        /* Secondary accent */
    --accent-pink: #ec4899;          /* Tertiary accent */
    --gradient-main: linear-gradient(135deg, #00d4ff 0%, #8b5cf6 50%, #ec4899 100%);
    --font-body: 'Inter', sans-serif;
    --font-heading: 'Outfit', sans-serif;
}
```

### Typing Phrases

Edit the `phrases` array in `script.js` to change the rotating titles:

```javascript
const phrases = [
    'Full-Stack Developer',
    'React Developer',
    'Node.js Developer',
    'Problem Solver',
    'Python Developer'
];
```

---

## 🛠️ Built With

- **HTML5** — Semantic, accessible markup
- **CSS3** — Custom properties, Grid, Flexbox, animations, glassmorphism
- **Vanilla JavaScript** — Intersection Observer API, async/await, DOM manipulation
- **[Google Fonts](https://fonts.google.com/)** — Inter & Outfit typefaces
- **[Font Awesome 6](https://fontawesome.com/)** — Icon library
- **[Web3Forms](https://web3forms.com/)** — Contact form email delivery

---

## 📦 Deployment

This is a static site — deploy anywhere!

| Platform | How to Deploy |
|----------|---------------|
| **GitHub Pages** | Push to `main` branch → Settings → Pages → Deploy from branch |
| **Vercel** | `npx vercel --prod` or connect your GitHub repo |
| **Netlify** | Drag & drop the folder, or connect your GitHub repo |
| **Render** | Create a new Static Site and point to your repo |

---

## 📄 Sections

| Section | Description |
|---------|-------------|
| **Hero** | Full-screen intro with typing animation, floating particles, and avatar |
| **About** | Bio with animated stat counters (projects, hackathons, achievements) |
| **Skills** | Categorized tech skills with animated progress bars and tags |
| **Projects** | Featured project cards — Taxi Booking, Full-Stack Apps, Smart Parking |
| **Experience** | Timeline of hackathons, education, and certifications |
| **Contact** | Working contact form (Web3Forms) + email, phone, location, Instagram |

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.

---

<div align="center">

**Designed & Developed by [Rohan Shrestha](https://instagram.com/rohan_stha/)**

⭐ Star this repo if you found it helpful!

</div>
