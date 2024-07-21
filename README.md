# Social Network Simulator

![Build Status](https://img.shields.io/github/actions/workflow/status/meisampw1384/Social-Network-Simulater-Django/ci.yml)
![Coverage](https://img.shields.io/codecov/c/github/meisampw1384/Social-Network-Simulater-Django)
![License](https://img.shields.io/github/license/meisampw1384/Social-Network-Simulater-Django)
![Version](https://img.shields.io/github/v/tag/meisampw1384/Social-Network-Simulater-Django)

This repository contains a Django-based social network simulator that allows users to create and manage profiles, post content, and interact with other users. The project is structured with the following apps:

### Apps

- **account**: Manages user profiles, including profile creation, editing, and authentication.
- **friendship**: Handles friend requests, accepting/declining friends, and managing friend lists.
- **posts**: Allows users to create, edit, delete, and share posts. Includes functionality for attaching files to posts.
- **social network**: The main project that integrates all the apps and provides the overall structure and routing.

### Key Features

- **User Profiles**: Create and manage detailed user profiles with customizable information.
- **Posts**: Users can create, edit, and delete posts with titles, captions, and additional metadata.
- **File Uploads**: Upload and attach files to posts, enhancing post content.
- **Post Sharing**: Share posts with other users within the network.
- **Friendship Management**: Send and manage friend requests, and maintain a list of friends.
- **Permissions**: Ensure that only authorized users can view and interact with specific posts.
- **API Endpoints**: RESTful API endpoints for managing posts, profiles, and friendships using Django REST Framework.

This project aims to simulate the core functionalities of a social network, providing a foundation for further development and experimentation.
