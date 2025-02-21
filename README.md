### **1. Backend (Django on AWS)**

- **Django + Django REST Framework (DRF)** for the API.
- **PostgreSQL** as the database (recommended for scalability).
- **Celery + Redis** for background tasks (e.g., rotating daily artwork).
- **S3 or Cloudinary** for storing images.
- **JWT authentication** for secure API access (shared across web and mobile).

### **2. Web Frontend (React or Angular)**

- Fetches data from the Django REST API.
- Can be deployed separately (e.g., Vercel, Netlify, or AWS S3 with CloudFront).

### **3. Mobile App (Kotlin + Jetpack Compose)**

- Fetches the same API as the web app.
- Uses **WorkManager** for scheduling daily notifications.
- Can store user preferences (e.g., favorite artworks) using **Room DB**.

### **4. Deployment**

- **Django on AWS**: EC2 for backend, RDS for DB, S3 for media.
- **React Web App**: Hosted separately (Vercel, S3, or CloudFront).
- **Kotlin App**: Published on the Play Store.

This setup ensures **easy maintenance and cross-platform compatibility**. Do you want a CI/CD pipeline for automatic deployments, or will you handle updates manually?
