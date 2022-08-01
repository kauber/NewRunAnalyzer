"""
All config classes
"""


class GlobalConfig:
    """Global config class"""

    input_data_path = "D:/PycharmProjectsDD/NewRunAnalyzer/data/Activities.csv"
    output_plots_folder = "D:/PycharmProjectsDD/NewRunAnalyzer/Reports/Plots/"
    output_report_folder = "D:/PycharmProjectsDD/NewRunAnalyzer/Reports/"
    rundate = "today"


class DataConfig:
    """Data config class"""

    cols = [
        "Date",
        "Title",
        "Distance",
        "Calories",
        "Time",
        "Avg HR",
        "Max HR",
        "Aerobic TE",
        "Avg Run Cadence",
        "Max Run Cadence",
        "Avg Pace",
        "Best Pace",
        "Total Ascent",
        "Total Descent",
        "Avg Stride Length",
        "Best Lap Time",
        "Moving Time",
        "Elapsed Time",
        "Min Elevation",
        "Max Elevation",
    ]


class LoggerConfig:
    """Logger Config class"""

    logger_name = "analyzer.log"
