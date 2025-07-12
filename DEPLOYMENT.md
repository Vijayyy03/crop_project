# 🌾 Smart Crop Advisor - Deployment Guide

This guide will help you deploy the Crop Recommendation System to various platforms.

## 🚀 Quick Deployment Options

### Option 1: Streamlit Cloud (Recommended)
1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository
5. Set the main file path to: `app.py`
6. Deploy!

### Option 2: Heroku
1. Create a Heroku account
2. Install Heroku CLI
3. Set environment variables:
   ```bash
   heroku config:set STREAMLIT_URL=https://your-app-name.herokuapp.com
   heroku config:set STREAMLIT_PORT=8501
   heroku config:set STREAMLIT_HOST=0.0.0.0
   heroku config:set SECRET_KEY=your-secret-key-here
   ```
4. Deploy using Heroku CLI

### Option 3: Railway
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub account
3. Select this repository
4. Set environment variables in Railway dashboard
5. Deploy!

## 🔧 Environment Variables

Set these environment variables for your deployment:

```bash
# Required for deployment
STREAMLIT_URL=https://your-app-url.com
STREAMLIT_PORT=8501
STREAMLIT_HOST=0.0.0.0
SECRET_KEY=your-secret-key-here
```

## 📁 Project Structure

```
crop_project/
├── app.py                 # Streamlit frontend (main app)
├── flask_app.py          # Flask authentication backend
├── deployment_config.py  # Deployment configuration helper
├── static/
│   └── styles.css       # Dark theme CSS
├── templates/
│   ├── login.html       # Login page
│   └── register.html    # Register page
├── model.pkl            # Trained ML model
├── standscaler.pkl      # Standard scaler
├── minmaxscaler.pkl     # MinMax scaler
└── requirements.txt     # Python dependencies
```

## 🌐 Deployment Platforms

### Streamlit Cloud
- **Pros**: Free, easy setup, perfect for Streamlit apps
- **Cons**: Limited to Streamlit only
- **Best for**: Quick demos and prototypes

### Heroku
- **Pros**: Full control, supports both Flask and Streamlit
- **Cons**: Requires credit card for verification
- **Best for**: Production applications

### Railway
- **Pros**: Free tier available, easy deployment
- **Cons**: Limited resources on free tier
- **Best for**: Small to medium applications

### Render
- **Pros**: Free tier, good performance
- **Cons**: Cold starts on free tier
- **Best for**: Cost-effective deployments

## 🔒 Security Notes

1. **Change the SECRET_KEY** for production
2. **Use HTTPS** in production
3. **Set up proper authentication** if needed
4. **Monitor your application** logs

## 🐛 Troubleshooting

### White Screen After Login
- Check if `STREAMLIT_URL` is set correctly
- Ensure the URL is accessible
- Check application logs for errors

### Port Issues
- Make sure `STREAMLIT_PORT` is set to 8501
- Check if the port is available on your platform

### Database Issues
- The app uses SQLite by default
- For production, consider using PostgreSQL or MySQL

## 📞 Support

If you encounter issues:
1. Check the application logs
2. Verify environment variables
3. Test locally first
4. Check platform-specific documentation

## ✨ Features

- 🌙 Beautiful dark theme
- 🤖 AI-powered crop recommendations
- 🔐 User authentication
- 📱 Responsive design
- ⚡ Fast and efficient
- 🎨 Modern UI/UX

Happy deploying! 🌾✨ 