# 📄 HTML - HyperText Markup Language

> The foundation of web development - learn to structure web content semantically.

## 📚 Table of Contents

- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
- [Key Topics](#key-topics)
- [Hands-On Practice](#hands-on-practice)
- [Projects](#projects)
- [Resources](#resources)
- [Next Steps](#next-steps)

## 🎯 Introduction

HTML (HyperText Markup Language) is the standard markup language for creating web pages. It describes the structure and content of a webpage using a system of tags and elements.

### What You'll Learn

- ✅ HTML document structure
- ✅ Semantic HTML elements
- ✅ Forms and input validation
- ✅ Accessibility best practices
- ✅ SEO fundamentals
- ✅ HTML5 features

### Prerequisites

- Basic computer literacy
- Text editor (VS Code recommended)
- Web browser (Chrome/Firefox recommended)

### Time to Complete

**Estimated:** 1-2 weeks (10-15 hours)

## 🧠 Core Concepts

### 1. HTML Document Structure

Every HTML document follows a basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

**Key Points:**
- `<!DOCTYPE html>` - Declares HTML5 document
- `<html>` - Root element
- `<head>` - Metadata and resources
- `<body>` - Visible content

### 2. Semantic HTML

Use meaningful tags that describe content:

```html
<header>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h1>Article Title</h1>
        <p>Article content...</p>
    </article>
    
    <aside>
        <h2>Related Content</h2>
    </aside>
</main>

<footer>
    <p>&copy; 2026 Your Name</p>
</footer>
```

**Benefits:**
- Better SEO
- Improved accessibility
- Easier maintenance
- Clearer code structure

### 3. Common HTML Elements

#### Text Elements
```html
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<p>Paragraph text</p>
<strong>Bold text</strong>
<em>Italic text</em>
<blockquote>Quote</blockquote>
```

#### Lists
```html
<!-- Unordered List -->
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<!-- Ordered List -->
<ol>
    <li>First</li>
    <li>Second</li>
</ol>
```

#### Links and Images
```html
<a href="https://example.com" target="_blank">External Link</a>
<img src="image.jpg" alt="Description" width="300" height="200">
```

### 4. Forms and Input

```html
<form action="/submit" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4"></textarea>
    
    <button type="submit">Submit</button>
</form>
```

**Input Types:**
- `text` - Single-line text
- `email` - Email address
- `password` - Password field
- `number` - Numeric input
- `date` - Date picker
- `checkbox` - Checkbox
- `radio` - Radio button
- `file` - File upload

## 📖 Key Topics

### 1. Document Structure
- [ ] DOCTYPE declaration
- [ ] HTML, head, and body tags
- [ ] Meta tags (charset, viewport, description)
- [ ] Title tag
- [ ] Link and script tags

### 2. Text Content
- [ ] Headings (h1-h6)
- [ ] Paragraphs
- [ ] Text formatting (strong, em, mark, del)
- [ ] Line breaks and horizontal rules
- [ ] Preformatted text

### 3. Links and Navigation
- [ ] Anchor tags
- [ ] Relative vs absolute URLs
- [ ] Target attribute
- [ ] Navigation menus
- [ ] Breadcrumbs

### 4. Images and Media
- [ ] Image tags and attributes
- [ ] Figure and figcaption
- [ ] Picture element for responsive images
- [ ] Video and audio elements
- [ ] Iframe for embedded content

### 5. Lists
- [ ] Unordered lists (ul)
- [ ] Ordered lists (ol)
- [ ] Description lists (dl)
- [ ] Nested lists

### 6. Tables
- [ ] Table structure (table, tr, td, th)
- [ ] Table headers and footers
- [ ] Column and row spanning
- [ ] Table accessibility

### 7. Forms
- [ ] Form element and attributes
- [ ] Input types
- [ ] Labels and fieldsets
- [ ] Form validation
- [ ] Submit and reset buttons

### 8. Semantic HTML5
- [ ] Header, nav, main, footer
- [ ] Article, section, aside
- [ ] Figure, figcaption
- [ ] Time, mark, progress

### 9. Accessibility
- [ ] ARIA attributes
- [ ] Alt text for images
- [ ] Semantic markup
- [ ] Keyboard navigation
- [ ] Screen reader compatibility

### 10. SEO Basics
- [ ] Title and meta descriptions
- [ ] Heading hierarchy
- [ ] Structured data
- [ ] Open Graph tags
- [ ] Canonical URLs

## 💻 Hands-On Practice

### Exercise 1: Personal Profile Page
Create a simple profile page with:
- Header with your name
- Profile image
- About section
- Skills list
- Contact information

### Exercise 2: Blog Post
Build a blog post page with:
- Article header
- Publication date
- Multiple paragraphs
- Images with captions
- Related articles sidebar

### Exercise 3: Contact Form
Create a contact form with:
- Name input
- Email input
- Subject dropdown
- Message textarea
- Submit button
- Form validation

### Exercise 4: Product Page
Design a product page with:
- Product images
- Product description
- Price and availability
- Add to cart button
- Customer reviews section

## 🚀 Projects

### Project 1: Personal Portfolio (Beginner)
**Goal:** Create a multi-page portfolio website

**Requirements:**
- Home page with introduction
- About page with bio
- Projects page with project cards
- Contact page with form
- Consistent navigation across pages

**Skills Practiced:**
- Document structure
- Semantic HTML
- Forms
- Links and navigation

**Time:** 3-5 hours

---

### Project 2: Recipe Website (Intermediate)
**Goal:** Build a recipe collection website

**Requirements:**
- Homepage with featured recipes
- Recipe detail pages
- Ingredient lists
- Step-by-step instructions
- Cooking time and difficulty
- Search functionality (HTML only)

**Skills Practiced:**
- Lists
- Tables
- Images
- Semantic structure

**Time:** 5-8 hours

---

### Project 3: Documentation Site (Advanced)
**Goal:** Create a technical documentation site

**Requirements:**
- Table of contents
- Multiple sections
- Code examples
- Navigation sidebar
- Search bar
- Breadcrumb navigation

**Skills Practiced:**
- Complex layouts
- Accessibility
- SEO optimization
- Semantic HTML

**Time:** 8-12 hours

## 📚 Resources

### Official Documentation
- [MDN HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [W3C HTML Specification](https://html.spec.whatwg.org/)
- [HTML5 Doctor](http://html5doctor.com/)

### Interactive Learning
- [freeCodeCamp HTML Course](https://www.freecodecamp.org/learn/responsive-web-design/)
- [Codecademy HTML Course](https://www.codecademy.com/learn/learn-html)
- [HTML Dog Tutorials](https://htmldog.com/guides/html/)

### Tools
- [HTML Validator](https://validator.w3.org/)
- [Can I Use](https://caniuse.com/) - Browser compatibility
- [HTML5 Outliner](https://gsnedders.html5.org/outliner/)

### Cheat Sheets
- [HTML Cheat Sheet](https://htmlcheatsheet.com/)
- [HTML5 Element Index](https://html5doctor.com/element-index/)

### Books
- "HTML and CSS: Design and Build Websites" by Jon Duckett
- "Learning Web Design" by Jennifer Robbins

## ✅ Checkpoint: HTML Mastery

Before moving to CSS, ensure you can:

- [ ] Create a valid HTML5 document structure
- [ ] Use semantic HTML elements appropriately
- [ ] Build accessible forms with validation
- [ ] Implement proper heading hierarchy
- [ ] Add images with appropriate alt text
- [ ] Create navigation menus
- [ ] Structure content with lists and tables
- [ ] Understand and apply SEO basics
- [ ] Validate HTML code
- [ ] Build a complete multi-page website

## 🎯 Next Steps

Once you've mastered HTML:

1. **Complete all practice exercises**
2. **Build at least one project**
3. **Validate your HTML code**
4. **Get feedback from peers**
5. **[Move to CSS →](../css/README.md)**

---

## 📝 Quick Reference

### Essential HTML Tags

| Tag | Purpose | Example |
|-----|---------|---------|
| `<h1>-<h6>` | Headings | `<h1>Title</h1>` |
| `<p>` | Paragraph | `<p>Text</p>` |
| `<a>` | Link | `<a href="url">Link</a>` |
| `<img>` | Image | `<img src="img.jpg" alt="desc">` |
| `<ul>/<ol>` | Lists | `<ul><li>Item</li></ul>` |
| `<div>` | Container | `<div>Content</div>` |
| `<span>` | Inline container | `<span>Text</span>` |
| `<form>` | Form | `<form>...</form>` |
| `<input>` | Input field | `<input type="text">` |
| `<button>` | Button | `<button>Click</button>` |

---

[← Back to Frontend](../README.md) | [CSS →](../css/README.md)