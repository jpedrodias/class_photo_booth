# Class-Photo-Booth
The objective of the **Class Photo Booth** application is to allow the capture of student photographs by class. The application facilitates the management, viewing, and export of photographs in an organized manner.

## � Project Statistics
- **Lines of Code**: 13,401 lines
- **Files**: 22 code files
- **Technologies**: Python Flask, HTML/CSS/JavaScript, Docker, Redis, PostgreSQL
- **Version**: 1.2 (updated on 09/07/2025)

## �📋 Features
```
📸 CLASS PHOTO BOOTH v1.2
Complete School Photograph Management System

  🔐 COMPLETE AUTHENTICATION SYSTEM
  ├─ 📧 Registration with email verification
  ├─ 🔑 Secure login with anti-brute force protection
  ├─ 🔄 Password recovery via email
  ├─ 👥 Role system (none/viewer/editor/admin)
  ├─ 🛡️ Automatic blocking of suspicious IPs
  ├─ 📊 Complete access audit
  └─ 👤 Default 'admin@example.com' user created

  👤 ADVANCED USER MANAGEMENT
  ├─ ➕ Account creation with email validation
  ├─ ✏️ Editing data and permissions
  ├─ 🔑 Password reset by administrators
  ├─ 🔒 Hierarchical role and permission management
  ├─ 📋 Complete administrative table
  ├─ ✅ Manual approval of new users
  └─ 🔒 Granular access control per functionality

  🏠 CLASS MANAGEMENT (Admin)
  ├─ ➕ Create classes
  ├─ ✏️ Edit class details
  ├─ 📋 View all classes
  ├─ 🗑️ Delete classes
  └─ 📊 Class statistics

  👨‍🎓 STUDENT MANAGEMENT
  ├─ ➕ Add students to classes
  ├─ ✏️ Edit student information
  ├─ 📋 View students by class
  ├─ 🗑️ Remove students
  ├─ 📊 Student statistics
  ├─ 🔍 Search and filter students
  ├─ 📝 Student notes system
  └─ 👁️ Quick notes preview on photo

  📸 PHOTO CAPTURE
  ├─ 📷 Camera integration
  ├─ 🖼️ Thumbnail generation
  ├─ 📁 Organized storage by class
  ├─ 🔄 Batch processing
  ├─ 📤 Drag-and-drop batch upload
  └─ 📊 Photo statistics

  📤 EXPORT AND DOWNLOAD
  ├─ 📦 ZIP download (originals/thumbnails)
  ├─ 📄 DOCX generation with professional layout
  ├─ 📊 Export statistics
  └─ 🔄 Automated export options

  ⚙️ ADMINISTRATIVE PANEL
  ├─ 👤 User management
  ├─ 🏠 Class management
  ├─ 📊 System statistics
  ├─ 🔧 Configuration settings
  ├─ 📋 Audit logs
  └─ 🛠️ System maintenance

  🔧 MONITORING AND MAINTENANCE
  ├─ 📊 Redis Server monitoring (memory, connections, latency)
  ├─ 👥 Active sessions monitoring
  ├─ 🗑️ Automatic cleanup of expired sessions
  ├─ 🧹 Manual cleanup buttons for Redis
  ├─ 📈 Performance statistics
  └─ 🔍 Detailed system logs
```

### 🐳 **Docker Installation**
```bash
# 1. Clone the repository
git clone https://github.com/jpedrodias/class_photo_booth.git
cd class_photo_booth

# 2. Configure .env
# Create .env based on the example below
# Edit .env with your settings

# 3. Build and run
docker-compose up -d

# 4. Add the first user (optional)
docker exec -it flaskapp /bin/bash -c "python ./init_database.py"

# 5. Access the application
# http://localhost (or configured port)
```

PS: Step 4 is optional, and in this case, the first user to create an account will be the Admin.

### 🔧 **First Access**
1. Access the application in the browser
2. Log in with the user `admin@example.com` and password `ChangeMe1#`
3. Change the administrator user password
4. Configure verification email
5. Import data via CSV (optional)
6. Explore the new Redis cleanup functionalities
7. Start using!

## 📚 Complete Documentation

For detailed technical documentation, consult the [`SPECIFICATIONS.md`](SPECIFICATIONS.md) file which includes:
- Complete system architecture
- Database models
- User flows
- Security considerations
- Deployment guides
- Monitoring and maintenance

## 🆕 **Version 1.2 New Features**
- **Automatic Redis Cleanup**: Automatic system for cleaning expired sessions
- **Manual Cleanup Buttons**: Interface for manual cleanup of obsolete records
- **Redis Monitoring**: Real-time monitoring panels
- **Drag-and-Drop Upload**: Photo upload via drag and drop
- **Performance Improvements**: Image processing optimizations
- **Enhanced Interface**: Better user experience
- **Student Notes System**: Functionality to add and view student notes
- **Smart Notes Button**: Optimized positioning on student photo

## 🤝 Contributions

Contributions are welcome! To contribute:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

## 📞 Support

For questions, suggestions, or issues:
- 📧 Email: 
- 🐛 Issues: [GitHub Issues](https://github.com/jpedrodias/class_photo_booth/issues)
- 📖 Documentation: [SPECIFICATIONS.md](SPECIFICATIONS.md)

---

**Class Photo Booth v1.2** - Developed with ❤️ to facilitate school photograph management
