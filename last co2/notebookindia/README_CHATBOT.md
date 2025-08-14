# 🤖 Energy Assistant Chatbot

## Overview
The Energy Assistant Chatbot is an AI-powered interface integrated into your Streamlit energy dashboard. It provides intelligent analysis and insights about your energy data, specifically designed to work with the `df_final_project3.csv` dataset.

## Features

### 🧠 Intelligent Analysis
- **Data Overview**: Get comprehensive statistics about your dataset
- **Energy Consumption Analysis**: Analyze patterns, trends, and anomalies
- **CO2 Emission Tracking**: Monitor environmental impact and sustainability metrics
- **Building Performance**: Compare different buildings and systems
- **Smart Recommendations**: AI-generated energy optimization suggestions

### 📊 Interactive Visualizations
- **Line Charts**: Time series analysis of energy consumption
- **Bar Charts**: Building and system comparisons
- **Heatmaps**: Correlation analysis between different metrics
- **Real-time Data**: Dynamic charts based on your selections

### 💬 Natural Language Interface
- Ask questions in plain English
- Get contextual responses based on your data
- Interactive conversation history
- Quick action buttons for common queries

## How to Use

### 1. Access the Chatbot
- Navigate to your Streamlit app
- Select "💬 Assistant IA" from the sidebar navigation
- The chatbot interface will load with your data

### 2. Ask Questions
You can ask the chatbot about:

#### Data Overview
- "Show me a data overview"
- "What's in my dataset?"
- "Give me dataset statistics"

#### Energy Analysis
- "Analyze energy consumption"
- "Show energy patterns"
- "What are the peak usage times?"

#### Building Performance
- "Compare building performance"
- "Which building uses the most energy?"
- "Show me building efficiency metrics"

#### CO2 and Environmental
- "Track CO2 emissions"
- "What's our environmental impact?"
- "Show sustainability metrics"

#### Visualizations
- "Create a line chart"
- "Show me a heatmap"
- "Visualize building comparisons"

#### Recommendations
- "Give me optimization suggestions"
- "How can I improve efficiency?"
- "What are the best practices?"

### 3. Quick Actions
Use the sidebar buttons for instant access to:
- 📊 Data Overview
- ⚡ Energy Analysis
- 💡 Get Recommendations

### 4. Interactive Charts
- Select chart type (line, bar, heatmap)
- Choose specific columns to visualize
- Generate charts on-demand
- View data samples

## Technical Details

### Data Requirements
- **File**: `df_final_project3.csv`
- **Location**: `notebookindia/data/` folder
- **Format**: CSV with date column and numeric energy/CO2 columns

### Supported Column Types
The chatbot automatically detects:
- **Energy Metrics**: Columns containing 'energy', 'power', 'consumption', 'kwh', 'mw'
- **CO2 Metrics**: Columns containing 'co2', 'carbon', 'emission'
- **Building/System Columns**: Columns containing building identifiers like 'acb', 'bh', 'db', 'gh', 'lb', 'lcb', 'srb'

### Dependencies
- `streamlit` - Web interface
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `plotly` - Interactive visualizations

## Installation

1. Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

2. Verify your data file is in the correct location:
```
notebookindia/
├── data/
│   └── df_final_project3.csv
├── pages/
│   └── chatbot.py
└── app.py
```

3. Run the Streamlit app:
```bash
cd notebookindia
streamlit run app.py
```

## Testing

Run the test script to verify everything works:
```bash
cd notebookindia
python test_chatbot.py
```

## Customization

### Adding New Response Types
Edit the `chatbot_response()` function in `chatbot.py` to add new keyword patterns and responses.

### Extending Visualizations
Modify the `create_energy_visualization()` function to add new chart types.

### Enhancing Recommendations
Update the `get_energy_recommendations()` function to include more sophisticated analysis algorithms.

## Troubleshooting

### Common Issues

1. **Data not loading**
   - Check file path: `notebookindia/data/df_final_project3.csv`
   - Verify CSV format and encoding
   - Check file permissions

2. **Import errors**
   - Ensure all dependencies are installed
   - Check Python path and module structure
   - Verify file locations

3. **Visualization errors**
   - Check data types (ensure numeric columns exist)
   - Verify date column format
   - Check for missing or invalid data

### Error Messages
- **"Dataset not found"**: Check file path and name
- **"Error loading data"**: Check CSV format and file integrity
- **"Could not generate chart"**: Verify column selection and data types

## Support

For issues or questions:
1. Check the test script output
2. Verify data file format and location
3. Check dependency versions
4. Review error logs in Streamlit

## Future Enhancements

Potential improvements:
- Machine learning-based predictions
- Advanced anomaly detection
- Integration with external APIs
- Export functionality for reports
- Multi-language support
- Voice interface integration 