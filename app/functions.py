def handler(event, context):
    param1 = event.get("param1")
    param2 = event.get("param2")

    # Доступ к контексту выполнения функции
    request_id = context.request_id
    function_name = context.function_name
    
    print(f"Function {function_name} handling request {request_id}")
    
    # Логика обработки данных
    result = {"message": f"Received param1: {param1} and param2: {param2}"}
    
    return result
