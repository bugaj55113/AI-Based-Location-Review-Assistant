# 🌍 Location Reviewer & AI Responder

This project is an evolving application aimed at assisting businesses or individuals in gathering reviews from specific locations and providing an automatic response to them using Artificial Intelligence. It's currently a desktop application built on `tkinter`, but the future goal is to transition it into a web application for better accessibility.

## 🌐 **Current Features**
- **Tkinter Based UI**: Provides an easy-to-navigate interface for users.
- **OpenAI Integration**: Utilizes the GPT-3.5 Turbo model from OpenAI for various AI-driven functionalities.
- **Sentiment Analysis**: Analyses the sentiment of the reviews using the VaderSentiment library.
- **Location Picker**: Integrates a browser to allow users to select locations on Google Maps.
- **Language Detection & Translation**: Can detect non-English reviews and translate them to English using the GPT-3.5 Turbo model.

## ⚙️ **Under Development**
- **Automated Response Generation**: Generate AI-powered responses based on the sentiment of the reviews.
- **Web Migration**: The plan is to migrate the application to a web platform for broader reach and ease of use.

## 💡 **How to Use**
1. Launch the application.
2. Load the desired file to analyze or pick a location.
3. Use the provided functionalities to count keywords, show popular characters/words, display sentiment, and more.

## 📚 **Libraries & Tools Used**
- **Tkinter**: For GUI creation.
- **OpenAI**: For AI-driven features, translation, and content generation.
- **VaderSentiment**: For sentiment analysis.
- **langdetect**: To detect the language of the review text.
- **cefpython3**: To embed the Chrome browser within the tkinter application for map functionalities.

## 🚀 **Future Enhancements**
- **Scalability**: Process and respond to reviews in bulk.
- **Custom Response Templates**: Allow users to set specific response templates for the AI to use.
- **Web Integration**: Transition from a desktop application to a web-based application.

## 📜 **License**
This project is currently under the [MIT License](LICENSE). Details can be found in the LICENSE file.

## 🖋 **Author**
- **Michał Bugaj**

---

*This project is ongoing, and feedback or contributions are always welcomed!*
