# Testing

Return back to the [README.md](README.md) file.

## Code Validation

[The W3C Markup Validation Service](https://validator.w3.org/) and [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) were used to validate every page of the project to ensure there were no syntax errors. The results clearly showed that the website stays in compliance with the standards and recommendations set by the World Wide Web Consortium.

[JSLint](https://www.jslint.com/), a static code analysis tool, was used to check if JavaScript source code complies with coding rules. No errors were found in this area.

### HTML Validation

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files. No errors were found when validating them by URI. 

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fhome) | ![home.html validation](documentation/home_html_validation.png) | Pass: No Errors |
| Sign Up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fsign_up) | ![sign_up.html validation](documentation/signup_html_validation.png) | Pass: No Errors |
| Sign In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fsign_in) | ![sign_in.html validation](documentation/signin_html_validation.png) | Pass: No Errors |
| Welcome | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fwelcome%2Fadmin) | ![welcome.html validation](documentation/welcome_html_validation.png) | Pass: No Errors |
| Blog | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fget_blog_posts) | ![blog_posts.html validation](documentation/add_post_html_validation.png) | Pass: No Errors |
| Read Blog Post | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fread_post%2F65cff8d14e3349ffe09cee93) | ![read_post.html validation](documentation/read_post_html_validation.png) | Pass: No Errors |
| Add Blog Post | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fadd_blog_post) | ![add_blog_post.html validation](documentation/add_post_html_validation.png) | Pass: No Errors |
| Edit Blog Post | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcome-code-with-me-43691c30d81d.herokuapp.com%2Fedit_blog_post%2F65cff8d14e3349ffe09cee93) | ![edit_blog_post.html validation](documentation/edit_post_html_validation.png) | Pass: No Errors |

To properly validate HTML pages with Jinja syntax for authenticated pages, I also utilized the "by input" validation method. It resulted in an error stating: "The `<button>` element must not appear as a descendant of an `<a>` element." It resulted in restructurring the affected buttons accordingly. Additionally, the validation flagged an issue indicating that a `<div>` element is not allowed as a child of a `<span>` element. However, I chose to disregard this suggestion because there is physically no `<div>` element within the `<span>` element where the issue was identified. The `<div>` element serves as a modal displayed upon clicking the `<span>` element.

### CSS Validation

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file. No errors were found.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator) | ![style.css validation](documentation/css_validation.png) | Pass: No Errors |

### JS Hint Testing

I have used [JSHint](https://jshint.com/) to identify potential errors in my JavaScript file. No errors were found.

| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![script.js](documentation/jshint_validation.png) | No errors found |

### Python Testing

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate my Python file.

| File | Screenshot | Notes |
| --- | --- | --- |
| app.py | ![screenshot](documentation/python_validation.png) | No errors found |

## Browser Compatibility

I have tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/edge.png) | Works as expected |
| Opera | ![screenshot](documentation/opera.png) | Works as expected |

## Responsiveness

I have tested my deployed project on multiple devices to check for responsiveness issues. It responds well to different screen sizes ensuring that users can access and navigate the content effortlessly, regardless of their chosen device. No design or functionality issues were found.

| Device | Screenshot 1 | Screenshot 2 | Screenshot 3 | Notes |
| --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot1](documentation/mobile_res1.png) | ![screenshot2](documentation/mobile_res2.png) | ![screenshot3](documentation/mobile_res3.png) | Works as expected |
| Tablet (DevTools) | ![screenshot1](documentation/tablet_res1.png) | ![screenshot2](documentation/tablet_res2.png) | ![screenshot3](documentation/tablet_res3.png) | Works as expected |
| Desktop | ![screenshot1](documentation/chrome.png) | ![screenshot2](documentation/desktop_res2.png) | ![screenshot3](documentation/desktop_res3.png) | Works as expected |

## Lighthouse Audit

I have tested my deployed project using the Lighthouse Audit tool to check for any major issues. 

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/home_audit_mobile.png) | Few warnings |
| Home | Desktop | ![screenshot](documentation/home_audit_desktop.png) | Some minor warnings |
| Welcome | Mobile | ![screenshot](documentation/welcome_audit_mobile.png) | Few warnings |
| Welcome | Desktop | ![screenshot](documentation/welcome_audit_desktop.png) | Some minor warnings |
| Sign Up | Mobile | ![screenshot](documentation/signup_audit_mobile.png) | Some minor warnings |
| Sign Up | Desktop | ![screenshot](documentation/signup_audit_desktop.png) | Some minor warnings |
| Sign In | Mobile | ![screenshot](documentation/signin_audit_mobile.png) | Some minor warnings |
| Sign In | Desktop | ![screenshot](documentation/signup_audit_desktop.png) | Some minor warnings |
| Blog Posts | Mobile | ![screenshot](documentation/blog_posts_audit_mobile.png) | Some minor warnings |
| Blog Posts | Desktop | ![screenshot](documentation/blog_posts_audit_desktop.png) | Some minor warnings |
| Read Post | Mobile | ![screenshot](documentation/read_post_audit_mobile.png) | Some minor warnings |
| Read Post | Desktop | ![screenshot](documentation/read_post_audit_desktop.png) | Some minor warnings |
| Add Blog Post | Mobile | ![screenshot](documentation/add_post_audit_mobile.png) | Few warnings |
| Add Blog Posst | Desktop | ![screenshot](documentation/add_post_audit_desktop.png) | Some minor warnings |
| Edit Blog Post | Mobile | ![screenshot](documentation/edit_post_audit_mobile.png) | Few warnings |
| Edit Blog Post | Desktop | ![screenshot](documentation/edit_post_audit_desktop.png) | Few warnings |

## User Stories Testing

### Client Goals

| User Stories | Completed? |
| --- | --- |
| As a client, I would like to provide users with accurate and up-to-date information about the current phase of the Moon. This could include displaying the Moon's appearance, percentage of illumination, distance to the Moon from Earth, and other relevant details. | ✔️ |
| As a client, I would like to educate users about the different phases of the Moon and the science behind them. It could provide explanations, diagrams, and relevant images to help users understand the lunar cycle. | ✔️ |
| As a client, I would like to provide a visual calendar that displays the Moon phases for a specific period (e.g., a year) that can help users track the Moon's changing appearance over time. | ✔️ |
| As a client, I would like to deliver all of the above in the form of a visually appealing, intuitive, responsive across different devices and easy to navigate website. | ✔️ |

### First Time User Goals

| User Stories | Completed? |
| --- | --- |
| As a first time user, I should be able to quickly and easily see the current phase of the Moon, whether it's a Full Moon, New Moon, Waxing Crescent, Waning Gibbous, etc. | ✔️ |
| As a first time user, I should be able to access more than just the current Moon Phase. I should be able to see additional information such as Moon illumination percentage, number of days through the cycle, number of days till the next Full Moon, etc. | ✔️ |
| As a first time user, I should be able to explore a calendar view that shows the Moon's phases for a specific period, helping me understand how the Moon's appearance changes over time. | ✔️ |
| As a first time user, I should be able to learn about the different phases of the Moon, their significance and why the Moon's appearance changes over time. | ✔️ |
| As a first time user, I should be able to navigate throughout the page in an easy, effortless and intuitive way. | ✔️ |
| As a first time user, I should be able to have a positive and enjoyable experience while browsing the website. | ✔️ |

### Returning/Frequent User Goals

| User Stories | Completed? |
| --- | --- |
| As a returning/frequent user, I should be able to continue tracking the Moon's changing phases to deepen my understanding of the Lunar Cycle. | ✔️ |
| As a returning/frequent user, I should be able to plan upcoming activities that align with specific Moon phases, such as outdoor events, photography sessions, or astronomical observations. | ✔️ |
| As a returning/frequent user, I should be able to revisit the website's settings to fine-tune my preferences, such as adjusting my time zone or choosing my favorite locations. | Take a look at the Future Implementations section in [README.md](README.md) file. |
| As a returning/frequent user, I should be able to share my own observations, photos, or experiences related to Moon phases within the website's community. | Take a look at the Future Implementations section in [README.md](README.md) file. |
| As a returning/frequent user, I should be able to stay informed about upcoming celestial events beyond Moon phases, such as meteor showers, planetary alignments, asteroids and comets. | Take a look at the Future Implementations section in [README.md](README.md) file. |
| As a returning/frequent user, I should be able to access the provider's social media accounts. | ✔️ |
| As a returning/frequent user, I should be able to offer feedback to the app developers based on my experiences, helping to shape future updates and improvements. | Take a look at the Future Implementations section in [README.md](README.md) file. |
