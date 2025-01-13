import streamlit as st
import streamlit_highcharts as hg

# Initialize Highcharts chart configurations
business_nature_chart = {
    "chart": {"type": "bar"},
    "title": {"text": "Business Nature Distribution"},
    "xAxis": {
        "categories": ["Beauty", "Arts and Crafts", "Agriculture", "Manufacturing", "Other"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Count", "data": [4, 3, 2, 2, 23]}
    ]
}

employee_count_chart = {
    "chart": {"type": "column"},
    "title": {"text": "Employee Count Distribution"},
    "xAxis": {
        "categories": ["1-5", "6-10", "10-15", "15-20"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Count", "data": [27, 3, 2, 1]}
    ]
}

ai_familiarity_chart = {
    "chart": {"type": "pie"},
    "title": {"text": "AI Familiarity Distribution"},
    "series": [
        {
            "name": "Familiarity",
            "colorByPoint": True,
            "data": [
                {"name": "No", "y": 14},
                {"name": "Yes", "y": 13},
                {"name": "Somewhat familiar", "y": 7}
            ]
        }
    ]
}

ai_investment_chart = {
    "chart": {"type": "bar"},
    "title": {"text": "AI Investment Willingness"},
    "xAxis": {
        "categories": ["Below R5000", "R6000-R10000", "R11000-R20000", "Above R20000"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Count", "data": [20, 7, 4, 3]}
    ]
}

ai_adoption_goal_chart = {
    "chart": {"type": "column"},
    "title": {"text": "AI Adoption Goals"},
    "xAxis": {
        "categories": ["Increase Revenue", "Enhance Decision-Making", "Improve Customer Experience", "Save Time"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Count", "data": [12, 8, 10, 5]}
    ]
}

business_nature_vs_ai_familiarity_chart = {
    "chart": {"type": "column"},
    "title": {"text": "Business Nature vs. AI Familiarity"},
    "xAxis": {
        "categories": ["Beauty", "Arts and Crafts", "Agriculture", "Manufacturing", "Other"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "No", "data": [2, 1, 1, 1, 9]},
        {"name": "Yes", "data": [2, 1, 1, 1, 8]},
        {"name": "Somewhat familiar", "data": [0, 1, 0, 0, 6]}
    ]
}

technological_challenges_vs_ai_interest_chart = {
    "chart": {"type": "bar"},
    "title": {"text": "Technological Challenges vs. AI Interest"},
    "xAxis": {
        "categories": ["Customer Retention", "Marketing", "Financial Planning", "Operational Efficiency"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Interested", "data": [10, 8, 6, 5]},
        {"name": "Not Interested", "data": [2, 1, 1, 1]}
    ]
}

preferred_learning_methods_vs_ai_familiarity_chart = {
    "chart": {"type": "bar"},
    "title": {"text": "Preferred Learning Methods vs. AI Familiarity"},
    "xAxis": {
        "categories": ["Workshops", "Webinars", "Consultations"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "No", "data": [5, 4, 3]},
        {"name": "Yes", "data": [4, 3, 6]},
        {"name": "Somewhat familiar", "data": [2, 3, 2]}
    ]
}

investment_vs_concerns_chart = {
    "chart": {"type": "bar"},
    "title": {"text": "Investment Willingness vs. Concerns About AI"},
    "xAxis": {
        "categories": ["Privacy", "Cost", "Complexity", "Expertise"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Below R5000", "data": [5, 8, 4, 3]},
        {"name": "R6000-R10000", "data": [2, 3, 1, 1]},
        {"name": "R11000-R20000", "data": [1, 1, 1, 1]},
        {"name": "Above R20000", "data": [1, 0, 0, 2]}
    ]
}

primary_goals_by_business_nature_chart = {
    "chart": {"type": "bar"},
    "title": {"text": "Primary Goals for AI Adoption by Business Nature"},
    "xAxis": {
        "categories": ["Beauty", "Arts and Crafts", "Agriculture", "Manufacturing", "Other"]
    },
    "yAxis": {"title": {"text": "Count"}},
    "series": [
        {"name": "Increase Revenue", "data": [2, 1, 2, 1, 6]},
        {"name": "Enhance Decision-Making", "data": [1, 1, 0, 0, 6]},
        {"name": "Improve Customer Experience", "data": [1, 1, 0, 1, 7]},
        {"name": "Save Time", "data": [0, 0, 0, 0, 5]}
    ]
}
business_nature_vs_ai_familiarity_heatmap = {
    "chart": {"type": "heatmap"},
    "title": {"text": "Business Nature vs AI Familiarity (Heatmap)"},
    "xAxis": {
        "categories": ["Beauty", "Arts and Crafts", "Agriculture", "Manufacturing", "Other"]
    },
    "yAxis": {
        "categories": ["No", "Yes", "Somewhat familiar"],
        "title": {"text": "AI Familiarity"}
    },
    "colorAxis": {"min": 0, "minColor": "#FFFFFF", "maxColor": "#7CB5EC"},
    "series": [
        {
            "name": "Familiarity Heatmap",
            "borderWidth": 1,
            "data": [
                [0, 0, 2], [0, 1, 2], [0, 2, 0],
                [1, 0, 1], [1, 1, 1], [1, 2, 1],
                [2, 0, 1], [2, 1, 1], [2, 2, 0],
                [3, 0, 1], [3, 1, 1], [3, 2, 0],
                [4, 0, 9], [4, 1, 8], [4, 2, 6]
            ]
        }
    ]
}

investment_vs_concerns_bubble_chart = {
    "chart": {"type": "bubble", "plotBorderWidth": 1, "zoomType": "xy"},
    "title": {"text": "Investment Willingness vs Concerns (Bubble Chart)"},
    "xAxis": {"title": {"text": "Investment Range"}, "categories": ["Below R5000", "R6000-R10000", "R11000-R20000", "Above R20000"]},
    "yAxis": {"title": {"text": "Concern Types"}, "categories": ["Privacy", "Cost", "Complexity", "Expertise"]},
    "series": [
        {
            "name": "Investment Bubbles",
            "data": [
                {"x": 0, "y": 0, "z": 5},
                {"x": 0, "y": 1, "z": 8},
                {"x": 0, "y": 2, "z": 4},
                {"x": 0, "y": 3, "z": 3},
                {"x": 1, "y": 0, "z": 2},
                {"x": 1, "y": 1, "z": 3},
                {"x": 1, "y": 2, "z": 1},
                {"x": 1, "y": 3, "z": 1},
                {"x": 2, "y": 0, "z": 1},
                {"x": 2, "y": 1, "z": 1},
                {"x": 2, "y": 2, "z": 1},
                {"x": 2, "y": 3, "z": 1},
                {"x": 3, "y": 0, "z": 1},
                {"x": 3, "y": 3, "z": 2}
            ]
        }
    ]
}
ai_tools_radar_chart = {
    "chart": {"polar": True, "type": "line"},
"pane": {
        "startAngle": 0,
        "endAngle": 360
    },
    "title": {"text": "Best AI Tools for Each Business Type"},
    "xAxis": {
        "categories": ["Chatbots", "Analytics", "Automation", "Recommendations"],
        "tickmarkPlacement": "on",
        "lineWidth": 0
    },
    "yAxis": {"gridLineInterpolation": "polygon", "lineWidth": 0, "min": 0},
    "series": [
        {"name": "Retail", "data": [5, 7, 6, 8], "pointPlacement": "on"},
        {"name": "Education", "data": [4, 6, 7, 5], "pointPlacement": "on"},
        {"name": "Healthcare", "data": [7, 5, 8, 6], "pointPlacement": "on"},
        {"name": "Technology", "data": [6, 8, 7, 5], "pointPlacement": "on"},
        {"name": "Agriculture", "data": [5, 4, 6, 7], "pointPlacement": "on"}
    ]
}
ai_tools_venn_chart = {
    "chart": {"type": "venn"},
    "title": {"text": "Overlap of Preferred AI Tools Across Business Types"},
    "series": [{
        "type": "venn",
        "data": [
            {"sets": ["Retail"], "value": 10, "name": "Retail"},
            {"sets": ["Education"], "value": 8, "name": "Education"},
            {"sets": ["Healthcare"], "value": 5, "name": "Healthcare"},
            {"sets": ["Technology"], "value": 7, "name": "Technology"},
            {"sets": ["Agriculture"], "value": 6, "name": "Agriculture"},
            {"sets": ["Retail", "Education"], "value": 4, "name": "Retail & Education"},
            {"sets": ["Healthcare", "Technology"], "value": 3, "name": "Healthcare & Technology"},
            {"sets": ["Agriculture", "Retail"], "value": 2, "name": "Agriculture & Retail"}
        ]
    }]
}




# Define the app layout
st.title("Survey Data Insights")

# Create a selection box for charts
chart_options = [
    "Business Nature Distribution",
    "Employee Count Distribution",
    "AI Familiarity Distribution",
    "AI Investment Willingness",
    "AI Adoption Goals",
    "Business Nature vs. AI Familiarity",
    "Technological Challenges vs. AI Interest",
    "Preferred Learning Methods vs. AI Familiarity",
    "Investment Willingness vs. Concerns About AI",
    "Primary Goals for AI Adoption by Business Nature",
    "Business Nature vs. AI Familiarity (Heatmap)",
    "Investment Willingness vs Concerns (Bubble Chart)",
"Best AI Tools for Each Business Type",
"Overlap of Preferred AI Tools Across Business Types"
]
selected_chart = st.selectbox("Select a Chart to Display:", chart_options)

if selected_chart == "Business Nature Distribution":
    st.subheader("Business Nature Distribution")
    hg.streamlit_highcharts(business_nature_chart, 600)
    #   hg.streamlit_highcharts(business_nature_chart, 600)
elif selected_chart == "Employee Count Distribution":
    st.subheader("Employee Count Distribution")
    hg.streamlit_highcharts(employee_count_chart, 600)
elif selected_chart == "AI Familiarity Distribution":
    st.subheader("AI Familiarity Distribution")
    hg.streamlit_highcharts(ai_familiarity_chart, 600)
elif selected_chart == "AI Investment Willingness":
    st.subheader("AI Investment Willingness")
    hg.streamlit_highcharts(ai_investment_chart, 600)
elif selected_chart == "AI Adoption Goals":
    st.subheader("AI Adoption Goals")
    hg.streamlit_highcharts(ai_adoption_goal_chart, 600)
elif selected_chart == "Business Nature vs. AI Familiarity":
    st.subheader("Business Nature vs. AI Familiarity")
    hg.streamlit_highcharts(business_nature_vs_ai_familiarity_chart, 600)
elif selected_chart == "Technological Challenges vs. AI Interest":
    st.subheader("Technological Challenges vs. AI Interest")
    hg.streamlit_highcharts(technological_challenges_vs_ai_interest_chart, 600)
elif selected_chart == "Preferred Learning Methods vs. AI Familiarity":
    st.subheader("Preferred Learning Methods vs. AI Familiarity")
    hg.streamlit_highcharts(preferred_learning_methods_vs_ai_familiarity_chart, 600)
elif selected_chart == "Investment Willingness vs. Concerns About AI":
    st.subheader("Investment Willingness vs. Concerns About AI")
    hg.streamlit_highcharts(investment_vs_concerns_chart, 600)
elif selected_chart == "Primary Goals for AI Adoption by Business Nature":
    st.subheader("Primary Goals for AI Adoption by Business Nature")
    hg.streamlit_highcharts(primary_goals_by_business_nature_chart, 600)
elif selected_chart == "Business Nature vs. AI Familiarity (Heatmap)":
    st.subheader("Business Nature vs. AI Familiarity (Heatmap)")
    hg.streamlit_highcharts(business_nature_vs_ai_familiarity_heatmap, 600)
elif selected_chart == "Investment Willingness vs Concerns (Bubble Chart)":
    st.subheader("Investment Willingness vs Concerns (Bubble Chart)")
    hg.streamlit_highcharts(investment_vs_concerns_bubble_chart, 600)
elif selected_chart == "Best AI Tools for Each Business Type":
    st.subheader("Best AI Tools for Each Business Type")
    hg.streamlit_highcharts(ai_tools_radar_chart, 600)
elif selected_chart == "Overlap of Preferred AI Tools Across Business Types":
    st.subheader("Overlap of Preferred AI Tools Across Business Types")
    hg.streamlit_highcharts(ai_tools_venn_chart,600)