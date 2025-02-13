# Product Recommendation System

## Overview
The **Product Recommendation System** is a machine learning-based solution that enhances user experience in e-commerce platforms by providing personalized product suggestions. The system combines **Association Rule Mining** (Apriori Algorithm) and **Customer Behavior Clustering** (DBSCAN) to deliver accurate and meaningful recommendations.

This project also includes a **Django-based e-commerce website** to demonstrate and deploy the recommendation system.

---
## Features
- **Association Rule Mining**: Discovers relationships between products using the **Apriori Algorithm**.
- **Customer Behavior Clustering**: Groups users with similar purchasing patterns using **DBSCAN clustering**.
- **Personalized Recommendations**: Integrates association rules and customer clusters to provide tailored suggestions.
- **E-commerce Web Application**: Built with **Django**, featuring a user-friendly interface with recommendation functionality.

---
## Technologies Used
- **Python** (for data processing & machine learning algorithms)
- **Apriori Algorithm** (for frequent itemset mining)
- **DBSCAN Clustering** (for customer segmentation)
- **Django** (for web development)
- **Kaggle Dataset** (for transactions and user purchase history)

---
## Project Structure
```
├── data/                     # Processed datasets for association rule mining & clustering
├── recommendation_system/    # Core logic for mining and clustering
│   ├── apriori.py           # Implementation of Apriori algorithm
│   ├── clustering.py        # DBSCAN clustering logic
│   ├── integration.py       # Combining mining and clustering results
├── ecommerce_website/       # Django-based e-commerce website
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, and other static files
│   ├── views.py             # Backend logic for recommendations
│   ├── models.py            # Database models
├── README.md                # Project documentation
└── requirements.txt         # Dependencies
```

---
## Installation & Setup
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/product-recommendation-system.git
   cd product-recommendation-system
   ```

2. **Set up a Virtual Environment (Optional but Recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Django Server:**
   ```sh
   cd ecommerce_website
   python manage.py runserver
   ```

5. **Access the Web Application:**
   Open a browser and go to `http://127.0.0.1:8000/`

---
## Usage
- **Homepage**: Displays available products.
- **Recommendation Page**: Provides personalized product recommendations.
- **User Interaction**: Customers receive recommendations based on previous transactions and shopping behavior.

---
## Future Improvements
- Implement **deep learning models** for more accurate recommendations.
- Enable **real-time updates** to improve recommendation accuracy.
- Conduct **A/B testing** for performance optimization.

---
## Contributors
- **Myself and Other Team Members**

---
## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---
## Contact
For any inquiries, feel free to reach out:
📧 Email: mhsanto03@gmail.com  
🔗 GitHub: [MohammadMehedy](https://github.com/MohammadMehedy)
