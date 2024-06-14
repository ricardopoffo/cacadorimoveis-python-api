from app.extensions import db

# Scrap(id, date_time_initial, date_time_end, real_estate_id, protocol)
class Scrap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time_initial = db.Column(db.DateTime, nullable=False)
    date_time_end = db.Column(db.DateTime, nullable=True)
    real_estate_id = db.Column(db.Integer, db.ForeignKey('real_estate.id'), nullable=False)
    protocol = db.Column(db.String(36), nullable=False)
   
    def __repr__(self):
        return f'<Scrap "{self.title}">'
    