from application import db

class Discounts(db.Model):
    __tablename__ = 'Discounts'
    discount_ID = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(30), nullable=False)
    paintjob_type = db.Column(db.String(30), nullable=False)
    discount_percent = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return ''.join([
            'Discount: ', paintjob_type, ' ', vehicle_type, ' ', ' - ', discount_percent , '%'
            ])