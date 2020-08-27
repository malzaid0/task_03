from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [{"restaurant_name" : "Murad", "food_type" : "Turkish"},
                    {"restaurant_name": "Kudu", "food_type": "Sandwich Sub"},
                    {"restaurant_name": "McDonald's", "food_type": "Garbage"},
                    ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {
            "restaurant_name": "Murad", "food_type": "Turkish" , "price_range": "Cheap"
        }
    }
    return render(request, 'detail.html', context)
