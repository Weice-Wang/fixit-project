# FixIt

## Description

FixIt is a web application that helps users track the items they own, especially products that require maintenance, repairs, warranty tracking, or recurring fixes.

The idea came from everyday life. Managing cars, home appliances, electronics, gaming devices, and tools can become difficult over time. It is easy to forget:

- warranty expiry dates
- repair history
- maintenance schedules
- replacement costs
- recurring issues

FixIt provides a simple way to organize and record all of this information in one place.

---

## Screenshot

![Homepage Screenshot](main_app/static/images/front_page.png)

---

### Deployed Application

https://fix-it-9dd47424d4a7.herokuapp.com/

### Planning Materials

- [Trello Board](https://trello.com/b/rFncigyk/fixit) (MVP, ERD, Wireframes)

---

## Technologies Used

- Django
- Python
- PostgreSQL
- HTML5
- CSS3
- Heroku
- GitHub

---

## Features

- User authentication
- Create, update, and delete items
- Maintenance tracking
- Warranty tracking
- Tag system
- User-specific item filtering

---

## Database Relationships

### One-to-Many

One item can have many maintenance records.

### Many-to-Many

Items can have multiple tags, and tags can belong to multiple items.

Example tags:

- urgent
- DIY
- recurring issue
- expensive
- temporary fix

---

## Attributions

- [Django Documentation](https://docs.djangoproject.com/)

---

## Future Enhancements

- Warranty expiry reminders
- Uploading receipts and photos
- Dashboard analytics
- AI-assisted repair suggestions
- Search and filtering system

---

## Author

Created by Weice Wang.
