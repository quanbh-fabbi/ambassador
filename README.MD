### 1. Remember: its' startproject app .
### 2. Add models
### 3. Docker
- setting mysql: port = 3306, host = db, pw = root
### 4. Database
- Connect: ambassador, root, root, 3309
- Add user.is_superuser = True
- Createsuperuse in docker exec bash
### 5. Add command to fix db waiting
- Add wait_for_db.py 
- "python manage.py wait_for_db &&" to CMD 
- docker-compose down -> up -d --build
### 6. 
### 7. Admin Authentication Endpoints
- POST /api/admin/register
- POST /api/admin/login
- GET /api/admin/logout
- POST /api/admin/logout
- PUT /api/admin/users/info
- PUT /api/admin/users/password

### 12. Static method
- A static method with @staticmethod won't have (self)

### 14. Logout
- Docker up not reload when code change? Check volumes