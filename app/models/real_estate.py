from app.extensions import db

# RealEstate(id, name, display_name, url_site, url_for_sale, url_to_rent, xpath_to_check_valid_page, card_xpath, properties_list_xpath, platform)
class RealEstate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    display_name = db.Column(db.String(240), nullable=False)
    url_site = db.Column(db.String(120), nullable=False)
    url_for_sale = db.Column(db.String(120), nullable=False)
    url_to_rent = db.Column(db.String(120), nullable=False)
    xpath_to_check_valid_page = db.Column(db.String(240), nullable=False)
    card_xpath = db.Column(db.String(240), nullable=False)
    properties_list_xpath = db.Column(db.String(240), nullable=False)
    platform = db.Column(db.String(120), nullable=False)
    scrap = db.relationship('Scrap', backref='real_estate', lazy=True)

    def __repr__(self):
        return f'<Real Estate "{self.title}">'
    