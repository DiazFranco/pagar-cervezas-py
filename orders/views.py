from django.http import JsonResponse
from django.utils.timezone import now
import json

stock = {
    "last_updated": "20240910 120000",
    "beers": [
        {"name": "Corona", "price": 115, "quantity": 2},
        {"name": "Quilmes", "price": 120, "quantity": 0},
        {"name": "Club Colombia", "price": 110, "quantity": 3}
    ]
}

order = {
    "created": "20240910 120000",
    "paid": False,
    "subtotal": 0,
    "taxes": 0,
    "discounts": 0,
    "items": [],
    "rounds": []
}


def get_order_status(request):
    return JsonResponse(order)


def create_order(request):
    try:
        body = json.loads(request.body)
        round_items = body.get("items", [])
        
        unavailable_items = []
        for item in round_items:
            beer_in_stock = next((beer for beer in stock["beers"] if beer["name"] == item["name"]), None)
            if beer_in_stock is None or beer_in_stock["quantity"] < item["quantity"]:
                unavailable_items.append(item["name"])

        if unavailable_items:
            return JsonResponse(
                {"error": f"Lo sentimos, no tenemos disponibles las siguientes cervezas: {', '.join(unavailable_items)}."},
                status=400
            )
        
        round_beer = {
            "created": now().strftime("%Y%m%d %H%M%S"),
            "items": round_items
        }
        order["rounds"].append(round_beer)
        
        subtotal = 0
        for item in round_items:
            for beer in stock["beers"]:
                if item["name"] == beer["name"]:
                    beer["quantity"] -= item["quantity"]
                    subtotal += beer["price"] * item["quantity"]
        
        order["subtotal"] = subtotal
        order["taxes"] = round(subtotal * 0.21, 0)
        order["discounts"] = 0
        
        return JsonResponse(order, status=200)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
