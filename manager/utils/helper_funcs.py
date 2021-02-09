

def get_store_link(request, store_id):
    domain = request.META["HTTP_HOST"]
    return f"http://{domain}/store/{store_id}"
