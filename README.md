# Yahoo Music Recommender

## Project Description

The Yahoo Music Recommender is a machine learning project aimed at developing a recommendation system for music tracks. This project uses collaborative filtering techniques to predict user preferences and recommend new music tracks based on user behavior and historical data. The system is designed to handle large datasets and provide personalized recommendations to enhance user experience.

This project leverages the Yahoo Music dataset, which contains a rich collection of user interactions with music tracks, including user ratings. The recommendation system employs matrix factorization methods to learn latent features of users and items, allowing for accurate predictions of user preferences.

### Why This Project?
- **Enhance User Experience**: Provide personalized music recommendations to users, increasing engagement and satisfaction.
- **Handle Large Datasets**: Efficiently process and analyze large-scale data to generate recommendations.
- **Machine Learning Application**: Apply collaborative filtering and matrix factorization techniques to solve real-world recommendation problems.

### Challenges and Future Work
- **Challenges**: Handling the sparsity of the user-item interaction matrix, optimizing model parameters for better accuracy, and ensuring scalability.
- **Future Features**: Incorporating additional data sources such as user demographics, implementing real-time recommendation updates, and exploring other recommendation algorithms like content-based filtering and hybrid methods.

### Stack
- Python 3.6 or higher
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- matplotlib

## Primary Methods Used

The final project utilized eight primary methods for making recommendations:

1. **Weighted Sums**: This method calculates the weighted sum of user ratings to generate recommendations. It considers the importance of each rating in the overall recommendation process.

2. **Matrix Factorization**: Matrix factorization techniques, such as Singular Value Decomposition (SVD), decompose the user-item interaction matrix into latent factors, allowing for the prediction of missing ratings.

3. **Logistic Regression**: A statistical method used for binary classification problems. In this project, logistic regression is employed to classify user preferences based on their interaction history.

4. **Decision Trees**: A non-parametric supervised learning method used for classification and regression. Decision trees are used to model user preferences by learning decision rules inferred from data features.

5. **Random Forest Classifiers**: An ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes for classification tasks. This method helps in improving the accuracy and robustness of the recommendations.

6. **Gradient Boosted Tree Classifiers**: An ensemble technique that builds multiple weak learners (decision trees) sequentially, with each tree correcting the errors of the previous ones. This method enhances the predictive performance of the model.

7. **Multi-layer Perceptron Classification**: A type of artificial neural network used for classification tasks. The multi-layer perceptron model captures complex patterns in the data to improve recommendation accuracy.

8. **Ensembling**: Combining the predictions from multiple models to improve overall performance. This method leverages the strengths of different algorithms to generate more accurate and reliable recommendations.

Each of these methods contributes to the robustness and accuracy of the Yahoo Music Recommender, providing a comprehensive approach to predicting user preferences and generating personalized music recommendations.
