from services.graph_service import GraphService


class GraphController:
    def get_graph_one_day(data: list) -> str:
        return GraphService.create_graph_one_day(data)
    
    
    def get_graph_multiple_days(data: list) -> str:
        return GraphService.create_graph_multiple_days(data)
