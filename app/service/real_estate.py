from app.extensions import db
from app.models.real_estate import RealEstate

def real_estate_create(data):
    if 'name' in data and 'url_for_sale' and 'url_to_rent' in data:
        real_estate = RealEstate(
            name=data["name"],
            display_name=data["display_name"],
            url_site=data["url_site"],
            url_for_sale=data["url_for_sale"], 
            url_to_rent=data["url_to_rent"],
            xpath_to_check_valid_page=data["xpath_to_check_valid_page"],
            card_xpath=data["card_xpath"],
            properties_list_xpath=data["properties_list_xpath"],
            platform=data["platform"]
        )
        db.session.add(real_estate)
        db.session.commit()

    return True