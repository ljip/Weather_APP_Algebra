import pandas
import io # Importing io module for working with streams
import base64 # Importing base64 module for encoding binary data to text

class GraphService:
    def create_graph_one_day(forecast_data: list) -> str:
        # Create a line plot of temperature data for one day and return a base64-encoded image URL
        data_frame = pandas.DataFrame(forecast_data)
        data_frame.set_index("datetime", inplace=True)

        # Convert the index to a datetime object
        data_frame.index = pandas.to_datetime(data_frame.index, format="%Y-%m-%d %H:%M:%S")
            
        line_plot = data_frame[["temp_min", "temp_max"]].plot()

        # Set the title and axis labels for the plot            
        line_plot.set_title("Daily forecast")
        line_plot.set_xlabel("Time")
        line_plot.set_ylabel("Celsius")
        
        # Set the x-axis tick labels to show time only
        line_plot.set_xticks(data_frame.index)
        line_plot.set_xticklabels(data_frame.index.strftime("%H:%M"))

        # Save the plot as a PNG image and return a base64-encoded image URL
        image = io.BytesIO()
        line_plot.figure.savefig(image, format="png")
        image.seek(0)
            
        image_type = "image/png"
        image_data = base64.b64encode(image.getvalue()).decode("ascii")
        return f"data:{image_type};base64,{image_data}"
    
    
    def create_graph_multiple_days(forecast_data: list) -> str:
        # Create a bar plot of temperature data for multiple days and return a base64-encoded image URL        
        data_frame = pandas.DataFrame(forecast_data)
        data_frame["date"] = pandas.to_datetime(data_frame["date"], format="%Y-%m-%d")
        data_frame.set_index("date", inplace=True)

        # Group the data by day and calculate the mean temperature values
        grouped = data_frame.groupby(pandas.Grouper(freq="D")).agg({
            "temp_min": "mean",
            "temp_max": "mean"
        })

        # Convert the index to a string in YYYY-MM-DD format
        grouped.index = grouped.index.strftime('%Y-%m-%d')

        # Create a bar plot of temperature data
        bar_plot = grouped.plot(kind="bar", rot=0, width=0.5)

        # Set the title and axis labels for the plot
        bar_plot.set_title("Daily forecast")
        bar_plot.set_xlabel("Date")
        bar_plot.set_ylabel("Celsius")
        
        # Set the y-axis limits to show temperature values up to 5 degrees higher than the current max
        current_min, current_max = bar_plot.get_ylim()
        bar_plot.set_ylim([current_min, current_max + 5])

        # Save the plot as a PNG image and return a base64-encoded image URL
        image = io.BytesIO()
        bar_plot.figure.savefig(image, format="png")
        image.seek(0)

        image_type = "image/png"
        image_data = base64.b64encode(image.getvalue()).decode("ascii")
        return f"data:{image_type};base64,{image_data}"