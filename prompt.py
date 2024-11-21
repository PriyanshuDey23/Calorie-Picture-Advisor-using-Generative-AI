PROMPT="""
Analyze the nutritional content of the uploaded food image and provide a detailed report, including:

- Food identification (dish name)
- Macro-nutrient breakdown (calories, protein, carbohydrates, fat)
- Micro-nutrient information (vitamins, minerals)
- Serving size and portion control suggestions
- Health score (healthy/unhealthy) with explanations
- Recommendations for modifications to make the dish healthier (if applicable)

Input Format: {uploaded_file}

Output Format:

Food Analysis Report
- Dish Name: [identified dish name]
- Nutritional Information:
    -    Calories: [value]
    -    Protein: [value]g
    -    Carbohydrates: [value]g
    -    Fat: [value]g
    -    Vitamins: [list]
    -    Minerals: [list]
- Serving Size: [suggested serving size]
- Health Score: [healthy/unhealthy]
- Health Notes: [brief explanation]
- Modification Suggestions: [optional recommendations]

Example Input: [Upload image of a burger]

Example Output:

Food Analysis Report

- Dish Name: Beef Burger with Cheese and Fries
- Nutritional Information:
    -    Calories: 750
    -    Protein: 35g
    -    Carbohydrates: 60g
    -    Fat: 40g
    -    Vitamins: Vitamin B12, Vitamin D
    -    Minerals: Iron, Calcium
- Serving Size: 1/2 burger, 1/2 serving of fries
- Health Score: Unhealthy
- Health Notes: High calorie and fat content due to cheese and fries.
- Modification Suggestions: Consider whole-grain bun, leaner beef, and roasted vegetables instead of fries.

You  will analyze the uploaded image, identify the dish, and provide a comprehensive nutritional report, along with health insights and suggestions for improvements.
Feel free to adjust or expand the prompt to suit your specific requirements!"
"""